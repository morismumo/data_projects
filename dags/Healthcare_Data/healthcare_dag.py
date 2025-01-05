from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from pendulum import datetime
import psycopg
import requests

# Function to fetch data from CMS API
def fetch_data():
    
    response = requests.get('https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data')
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    return data

# Function to insert data into a db
def insert_data():
  hook = PostgresHook(postgres_conn_id='postgres')
  #postgres_url = 'postgres://postgres:postgres@host.docker.internal:5434/healthdb'
  conn = hook.get_conn()
  mydata = fetch_data()
  with conn.cursor() as cur:
    # Create table if it doesn't exist
    cur.execute("""
      CREATE TABLE IF NOT EXISTS therapy_providers (
          id SERIAL PRIMARY KEY,
          enrollment_id VARCHAR(50), 
          legal_business_name VARCHAR(255),
          street_address_line_1 VARCHAR(255),
          street_address_line_2 VARCHAR(255),
          city VARCHAR(255),
          state VARCHAR(2),
          zip_code VARCHAR(20), 
          practice_location_phone VARCHAR(25), 
          specialty_name VARCHAR(255),
          geographic_location_type_description VARCHAR(255),
          geographic_location_city_name VARCHAR(255), 
          geographic_location_state_code VARCHAR(2),
          geographic_location_zip_code VARCHAR(20),
          state_county_name VARCHAR(255) 
      )
    """)

    # Insert data using a single execute_many for efficiency
    insert_sql = """
      INSERT INTO therapy_providers (
          enrollment_id,
          legal_business_name,
          street_address_line_1,
          street_address_line_2,
          city,
          state,
          zip_code,
          practice_location_phone,
          specialty_name,
          geographic_location_type_description,
          geographic_location_city_name,
          geographic_location_state_code,
          geographic_location_zip_code,
          state_county_name
      ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data_tuples = [(item.get('Enrollment ID'),
                    item.get('Legal Business Name'),
                    item.get('Street Address Line 1'),
                    item.get('Street Address Line 2'),
                    item.get('City'),
                    item.get('State'),
                    item.get('ZIP Code'),
                    item.get('Practice Location Phone Number'),
                    item.get('Specialty Name'),
                    item.get('Geographic Location Type Description'),
                    item.get('Geographic Location City Name'),
                    item.get('Geographic Location State Code'),
                    item.get('Geographic Location ZIP Code'),
                    item.get('State County Name')) for item in mydata]
    cur.executemany(insert_sql, data_tuples)

  conn.commit()

with DAG(
    dag_id='Healthcare_data_to_Postgres',
    start_date=datetime(2024, 12, 17),
    description='run a dag that pulls data from a data source api, and uploads it to a postgres container',
    schedule_interval=None,
) as dag:

    # # Start Postgres container if not up already
    # start_postgres = BashOperator(
    # task_id='start_postgres',
    # bash_command='docker compose -f ./dags/Healthcare_Data/compose.yml up -d && sleep 30',
    # dag=dag,
    # )

    # Extract data from our source
    extract_data = PythonOperator(
        task_id='extract_data_from_api',
        python_callable=fetch_data,
        dag=dag
    )

    # Connect to Postgres and insert data
    connect_and_insert = PythonOperator(
        task_id='connect_and_insert_data',
        python_callable=insert_data,
        provide_context=True,
        dag=dag
    )

# connect to db and insert data
extract_data >> connect_and_insert