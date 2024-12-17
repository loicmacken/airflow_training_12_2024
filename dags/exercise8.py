from airflow import DAG, Dataset
from airflow.operators.empty import EmptyOperator

from datetime import datetime, timedelta

intermediate_dataset = Dataset(
    "https://httpstat.us/200",  # URI
)

with DAG(
    dag_id="produce",
    start_date=datetime.now(),
    schedule_interval=timedelta(seconds=10),
):
    do_the_thing = EmptyOperator(
        task_id="do_the_thing", 
        outlets=[intermediate_dataset]
    )

with DAG(
    dag_id="consume",
    start_date=datetime.now(),
    schedule=[intermediate_dataset],
):
    consume_the_thing = EmptyOperator(
        task_id="consume_the_thing"
    )