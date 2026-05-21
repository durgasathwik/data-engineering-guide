from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

def on_failure_callback(context):
    task_id = context['task_instance'].task_id
    execution_date = context['ds']
    print(f"Failed: {task_id} - {execution_date}")

def extract_data(**context):
    warehouse_url = Variable.get('WAREHOUSE_URL', default_var="default_url")
    pass

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
