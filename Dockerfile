FROM apache/airflow:2.1.4

USER root
RUN apt-get update && apt-get install -y \
    vim \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /usr/local/airflow/dags/
COPY plugins/ /usr/local/airflow/plugins/
COPY config/ /usr/local/airflow/config/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["webserver"]
