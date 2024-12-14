import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.docker_operator import DockerOperator

#step1 fire up a db instance using a compose.yml file and connect to the db or create one(init.sql script) if doesn't exit
#step2 request data from source api to a json file in our directory folder using a python file
#step3 ensure the json files are timebased as to allow incremental data loading
#step4 clean the data from the json file and load it to our db
#step5 we can connect the db to a spark instance for more data processing

