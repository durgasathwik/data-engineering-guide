import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def on_failure(context):
    task_id = context['task_instance'].task_id
    exec_date = context['ds']
    print(f"Failure: {task_id} on {exec_date}")

def check_file_arrival(**context):
    date = context['ds']
    path = f'/data/shipments/{date}.csv'
    if not os.path.exists(path):
        raise FileNotFoundError(f'Missing file: {path}')

def validate_records(**context):
    pass

def transform_records(**context):
    pass

def load_to_warehouse(**context):
    date = context['ds']
    
    delete_query = f"DELETE FROM warehouse.shipments WHERE execution_date = '{date}'"
    insert_query = f"INSERT INTO warehouse.shipments SELECT * FROM staging.shipments WHERE execution_date = '{date}'"

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
