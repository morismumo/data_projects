from dotenv import dotenv_values
import psycopg2
import requests

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
