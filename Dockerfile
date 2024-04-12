FROM python:3.8-slim-buster

# Установить Java для PySpark
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Установить переменные среды для PySpark
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
ENV PATH=$PATH:$JAVA_HOME/bin

RUN pip install pyspark==3.1.2

WORKDIR /app
COPY . /app