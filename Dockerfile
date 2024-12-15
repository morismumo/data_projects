FROM apache/airflow:2.10.3
WORKDIR /home/mumo/dataprojects
COPY dags/Healthcare_Data .
ENV FILE .env
RUN pip install --upgrade pip
RUN pip install python-dotenv pendulum