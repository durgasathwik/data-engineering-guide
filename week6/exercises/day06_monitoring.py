from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

# Day 6: Monitoring, Callbacks, and Variables

def on_failure_callback(context):
    task_id = context['task_instance'].task_id
    execution_date = context['ds']
    print(f"FAILED: Task {task_id} failed on execution date {execution_date}")

def extract_data(**context):
    # Fetch a variable from Airflow metadata database
    # (In a real environment, you'd use Variable.get('WAREHOUSE_URL'))
    warehouse_url = "dummy_warehouse_url" 
    print(f"Connecting to warehouse at: {warehouse_url}")

with DAG(
    dag_id='day06_monitoring',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args={
        'on_failure_callback': on_failure_callback
    }
) as dag:

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )
