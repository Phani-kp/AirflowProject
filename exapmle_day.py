from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello World")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')
    hello_task = PythonOperator(task_id='hello_task', python_callable=hello_world)
    end = DummyOperator(task_id='end')

    start >> hello_task >> end
