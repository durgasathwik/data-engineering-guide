from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def load_idempotent(**context):
    execution_date = context['ds']
    
    delete_query = f"DELETE FROM shipments WHERE shipment_date = '{execution_date}'"
    insert_query = f"INSERT INTO shipments SELECT * FROM staging WHERE shipment_date = '{execution_date}'"

with DAG(
    dag_id='day04_idempotency',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id='load_warehouse_idempotent',
        python_callable=load_idempotent
    )
