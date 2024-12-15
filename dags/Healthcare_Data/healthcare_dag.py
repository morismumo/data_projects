from dotenv import dotenv_values
import psycopg2
import requests

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from pendulum import datetime

dag = DAG(
    dag_id='Fetch_and_load_CMS_data_to_Postgres_db',
    start_date=datetime(2024,12,15),
    schedule_interval=None,
)

# Now to fetch and load data as json
url = 'https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data'
def _fetch_and_load_data(url):
    response = requests.get('url')
    #let's check if response is a success -- then load the data to json
    if response.status_code == 200:
        data = response.json()
    else:
        print('failed: ', response.status_code)

# Lets define the environment variables dict
db_config = dotenv_values('.env')

# To connect to our postgres db instance
def _connect_to_db(db_config):

    conn = psycopg2.connect(
        database=db_config['DB_NAME'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        host=db_config['DB_HOST'],
        port=db_config['DB_PORT']
    )
    return conn

#To connect to the database
conn = _connect_to_db(db_config)
table_name = 'therapy_providers'
# next is we use the database connection to insert data/execute queries
# we start by creating a cursor or use context manager
def _data_insert():
    with conn.cursor() as cur:
        def insert_data(conn, cur, table_name, data):
            try:
                query = f"INSERT INTO {table_name} VALUES %S"
                cur.execute(query, data)
                conn.commit()
            except (Exception, psycopg.DatabaseError) as error:
                print(f"Error: {error}")
                conn.rollback()

start_db_container = BashOperator(
    task_id='postgres_container_up',
    bash_command="docker compose up -d",
    dag=dag,
)

extract_data = PythonOperator(
    task_id='download_data_from_api',
    python_callable='extract_load._fetch_and_load_data',
    dag=dag,
)
    

connect_and_insert = PythonOperator(
    task_id = 'connnect_to_postgres_container',
    python_callable='extract_load._data_insert',
    dag=dag,
)

start_db_container >> extract_data >> connect_and_insert