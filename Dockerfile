FROM apache/airflow:2.9.3

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install --no-cache-dir pandas faker