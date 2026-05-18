from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def ingest_data():
    pass

def validate_data():
    pass

def report_data():
    pass

with DAG(
    dag_id='day02_basic_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id='ingest',
        python_callable=ingest_data
    )

    validate = PythonOperator(
        task_id='validate',
        python_callable=validate_data
    )

    report = PythonOperator(
        task_id='report',
        python_callable=report_data
    )

    [ingest, validate] >> report
