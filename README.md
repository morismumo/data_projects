# datapipelineprojects
 This is the main folder for all the data pipeline projects.

 Each project will have a different objective and will have its own subfolder.

"Tell me and I forget. Teach me and I remember. Involve me and I learn." - Richard Branson

To run any of the projects we need to run an airflow instance
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'
-- change the yaml file where load examples is true to false

This assumes that docker is already running on your development setup

Setting the right Airflow user on linux
$ mkdir -p ./dags ./logs ./plugins ./config
$ echo -e "AIRFLOW_UID=$(id -u)" > .env

initialising the database
$ docker compose up airflow-init

now lets run the docker-compose.yml to run airflow
$ docker compose up -d