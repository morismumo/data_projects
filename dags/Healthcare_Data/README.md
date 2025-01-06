To run this dag successfully, you need to first run the compose.yml file in dags/Healthcare_Data/compose.yml.

    $ docker compose up -d

This will initiate our database for the project
To check if the postgres database is running and accepting connection

    $ docker ps
    -- check if the container is running: name ending with db_02
    $ docker logs <container id>
    -- look for LOG: database system is ready to accept connections

but first we need to test for connection in airflow UI connections

    1. connection ID : postgres
    2. host : 172.17.0.1
    -- the host is defined in the docker compose file
    3. login : postgres
    4. password : postgres
    5. port : 5434
    -- you can now test the connection
    -- airflow will display 'connection succeful' at the top of the webpage if well configured

You can now run the dag from airflow UI dags list
    
     **Healthcare_data_to_Postgres**