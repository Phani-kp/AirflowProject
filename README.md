# AirflowProject

This is a sample Apache Airflow project.

## Setup

1. Build the Docker image:

    ```sh
    docker build -t airflow_project .
    ```

2. Run the Docker container:

    ```sh
    docker run -d -p 8080:8080 airflow_project
    ```

3. Access the Airflow web server at [http://localhost:8080](http://localhost:8080).

## DAGs

- `example_dag`: A simple DAG that prints "Hello World".
- `another_dag`: A dummy DAG that runs hourly.

## Custom Plugins

- `custom_operator.py`: An example of a custom operator.
