![Version](https://img.shields.io/badge/Apache%20Airflow%20ver.%3A-2.4.1-brightgreen.svg)
![Version](https://img.shields.io/badge/PostgreSQL%20ver.%3A-14-brightgreen.svg)
![Version](https://img.shields.io/badge/Redis%20ver.%3A-7.0.5-brightgreen.svg)

## Information

Apache Airflow Docker Compose Example for local using.
After install & run, you will have:
1. Apache Airflow with Celery Executor
2. 2 Workers
3. Test Dummy DAG

Docker compose volumes structure:
```
Repository
└───airflow
    ├───dags    # DAGs
    ├───files   # Files
    ├───logs    # Airflow logs
    └───plugins # Airflow plugins
```

## Installation

1. Install Docker
2. Install Docker Compose

## Usage
1. Cloning repository
2. Start Containers in “detached” mode
    ```shell
    $ docker compose up -d
    ```

3. After containers are UP, you can open webpages of Airflow & Flower:

    * Apache Airflow web address: http://localhost:8080 (login: airflow, password: airflow)
    * Flower web address: http://localhost:5555