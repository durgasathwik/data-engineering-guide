from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Day 4: Idempotency

# Non-idempotent example (Do not use in production)
def load_non_idempotent():
    # INSERT INTO shipments SELECT * FROM staging
    pass

# Idempotent example: DELETE-then-INSERT
def load_idempotent(**context):
    execution_date = context['ds']
    print(f"Executing idempotent load for date: {execution_date}")
    
    # DELETE FROM shipments WHERE shipment_date = '{execution_date}'
    print(f"Deleted existing records for {execution_date}")
    
    # INSERT INTO shipments SELECT * FROM staging WHERE shipment_date = '{execution_date}'
    print(f"Inserted fresh records for {execution_date}")

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
