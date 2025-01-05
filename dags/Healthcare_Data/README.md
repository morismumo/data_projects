To run this dag successfully, you need to first run the compose.yml file in dags/Healthcare_Data/compose.yml.

    $ docker compose up -d

This will initiate our database for the project
To check if the postgres database is running and accepting connection

    $ docker ps
    -- check if the container is running: name ending with db_02
    $ docker logs <container id>
    -- look for LOG: database system is ready to accept connections

You can now run the dag from airflow UI dags list
    
     **Healthcare_data_to_Postgres**
