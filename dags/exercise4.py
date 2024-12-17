from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="delay",
    start_date=datetime.now(),
    description="This DAG will delay.",
    schedule=None,
):

    http_sensor = HttpSensor(task_id="http_sensor", endpoint="", http_conn_id="http_delayed")

    test = EmptyOperator(task_id="test")

    http_sensor >> test