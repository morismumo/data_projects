FROM apache/airflow:2.10.3
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt