# Data_Projects
 This is the main folder for all the data pipeline projects.

 Each project will have a different objective and will have its own subfolder in the dags directory.

**Learning by Doing**

    "Tell me and I forget. Teach me and I remember. Involve me and I learn." - Richard Branson

# Getting Started

**Prerequisites**

1. [Install Docker Desktop](https://docs.docker.com/get-started/get-docker/)
2. Clone this repository onto your local machine

To run any of the projects we need to run our airflow instance in docker.
Clone this directory to your local environment with the following command:

    $ git clone <repository_url>

Navigate to the data_projects/airflow directory where there is this docker-compose.yml file and run the command below:

    $ mkdir logs dags plugins && docker compose up -d

This assumes that docker is already installed and a docker daemon is running on your development setup (local machine)!

If successful you should see 3 docker containers running;

    $ docker ps

An airflow scheduler, a webserver, and a postgres container

The airflow webserver is available on localhost:8080 admin:airflow password:airflow

Each dag in ./airflow/dags directory will have its own README to be able to run the dag successfully

**Dags' README files list:**
1. [Healthcare_Data](/airflow/dags/Healthcare_Data/README.md)
