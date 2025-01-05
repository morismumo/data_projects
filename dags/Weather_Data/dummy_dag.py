from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def check_condition():
    """
    This function simulates a condition check. 
    """
    import random
    return random.choice([True, False])

with DAG(
    dag_id='conditional_task_flow',
    start_date=datetime(2024, 12, 21),
    schedule_interval=None,
    catchup=False,
) as dag:

    start = DummyOperator(task_id='start')
    
    check_condition_task = PythonOperator(
        task_id='check_condition',
        python_callable=check_condition
    )

    task_a = DummyOperator(task_id='task_a')
    task_b = DummyOperator(task_id='task_b')
    task_c = DummyOperator(task_id='task_c')
    task_d = DummyOperator(task_id='task_d')

    start >> check_condition_task

    check_condition_task >> task_a
    check_condition_task >> task_b

    task_a >> task_c
    task_a >> task_d

    task_b >> task_c
    task_b >> task_d