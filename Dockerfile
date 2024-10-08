FROM apache/airflow:2.7.2-python3.11
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
USER root
RUN apt-get update
RUN apt-get install -y git
RUN apt-get clean

