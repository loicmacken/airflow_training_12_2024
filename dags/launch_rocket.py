from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="launch_rocket",
    start_date=datetime.now() - timedelta(days=90),
    description="This DAG will launch a rocket to Mars",
    schedule="0 0 */3 * *",
):
    procure_rocket_material = EmptyOperator(task_id="procure_rocket_material")
    procure_fuel = EmptyOperator(task_id="procure_fuel")
    build_stage_1 = EmptyOperator(task_id="build_stage_1")
    build_stage_2 = EmptyOperator(task_id="build_stage_2")
    build_stage_3 = EmptyOperator(task_id="build_stage_3")
    launch = EmptyOperator(task_id="launch")

    procure_rocket_material >> [build_stage_1, build_stage_2, build_stage_3]
    procure_fuel >> build_stage_3
    [build_stage_1, build_stage_2, build_stage_3] >> launch