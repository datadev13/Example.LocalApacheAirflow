from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

with DAG('test_dag', start_date=datetime(2022, 1, 1)) as dag:
    op = DummyOperator(task_id='dtd')