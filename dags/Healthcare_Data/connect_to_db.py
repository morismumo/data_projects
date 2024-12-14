from dotenv import dotenv_values
import psycopg

#dotenv_path = '/path/to/our/.env/' this is necessary if we have multiple .env files
#load_dotenv(dotenv_path=dotenv_path)
#load_dotenv()   Loading environment variables from .env file defined in our root directory

# Lets define the environment variables dict
db_config = dotenv_values('.env')

# To connect to our postgres db instance
def connect_to_db(db_config):

    conn = psycopg.connect(
        database=db_config['DB_NAME'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        host=db_config['DB_HOST'],
        port=db_config['DB_PORT']
    )
    return conn

#To connect to the database
conn = connect_to_db(db_config)

# next is we use the database connection to insert data/execute queries