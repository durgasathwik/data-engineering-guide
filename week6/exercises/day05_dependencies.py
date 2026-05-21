from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def check():
    pass

def val_row():
    pass

def val_schema():
    pass

def load():
    pass

with DAG(
    dag_id='day05_dependencies',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    file_check = PythonOperator(task_id='file_check', python_callable=check)
    row_validation = PythonOperator(task_id='row_validation', python_callable=val_row)
    schema_validation = PythonOperator(task_id='schema_validation', python_callable=val_schema)
    load_warehouse = PythonOperator(task_id='load_warehouse', python_callable=load)

    file_check >> [row_validation, schema_validation] >> load_warehouse
