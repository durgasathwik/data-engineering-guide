from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Day 3: Retries, SLAs, and Task States

def ingest_task():
    print("Ingesting with high retry logic...")

def transform_task():
    print("Transforming with standard retry logic...")

with DAG(
    dag_id='day03_retries_slas',
    start_date=datetime(2024, 1, 1),
    schedule_interval='0 2 * * *',
    catchup=False,
    default_args={
        'sla': timedelta(hours=3) # SLA of 3 hours on the entire DAG
    }
) as dag:

    ingest = PythonOperator(
        task_id='ingest',
        python_callable=ingest_task,
        retries=5,
        retry_delay=timedelta(minutes=20)
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_task,
        retries=2,
        retry_delay=timedelta(minutes=5)
    )

    ingest >> transform
