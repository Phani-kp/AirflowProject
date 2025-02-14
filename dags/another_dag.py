from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('another_dag', default_args=default_args, schedule_interval='@hourly') as dag:
    start = DummyOperator(task_id='start')
    process = DummyOperator(task_id='process')
    end = DummyOperator(task_id='end')

    start >> process >> end
