from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# Day 7 Mini Project: Logistics Company Daily Shipment Pipeline

def on_failure(context):
    task_id = context['task_instance'].task_id
    exec_date = context['ds']
    print(f"ALERT: FAILED Task {task_id} on {exec_date}")

def check_file_arrival(**context):
    date = context['ds']
    path = f'/data/shipments/{date}.csv'
    # Simulation: Normally we would check if os.path.exists(path)
    print(f'Checking for shipment file: {path}')
    # To test retry behavior, one could raise FileNotFoundError here.

def validate_records(**context):
    date = context['ds']
    print(f'Validating records for {date} (checking nulls, row counts)')

def transform_records(**context):
    date = context['ds']
    print(f'Transforming shipments for {date} (standardize, deduplicate)')

def load_to_warehouse(**context):
    date = context['ds']
    print(f'Idempotent Load for {date}:')
    print(f'1. DELETE existing records for {date}')
    print(f'2. INSERT transformed records for {date}')

with DAG(
    dag_id='logistics_daily_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='0 2 * * *',
    catchup=False,
    default_args={
        'retries': 3,
        'retry_delay': timedelta(minutes=15),
        'sla': timedelta(hours=4),
        'on_failure_callback': on_failure
    }
) as dag:

    file_check = PythonOperator(
        task_id='check_file_arrival',
        python_callable=check_file_arrival,
        retries=5,
        retry_delay=timedelta(minutes=20)
    )

    validate = PythonOperator(
        task_id='validate_records',
        python_callable=validate_records
    )

    transform = PythonOperator(
        task_id='transform_records',
        python_callable=transform_records
    )

    load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_to_warehouse
    )

    file_check >> validate >> transform >> load
