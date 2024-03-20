
from __future__ import annotations

import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor

DAG_ID = "airflow_airbyte"
airbyte_con_id = "airbyte_testing"
connect_id = "9c87cf8f-a7b9-46a4-b658-da61e74f74ed"

with DAG(
    dag_id=DAG_ID,
    schedule=None,
    start_date=datetime(2021, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    tags=["example"],
    catchup=False,
) as dag:
    sync_source_destination = AirbyteTriggerSyncOperator(
        task_id="airbyte_sync_source_dest_example",
        airbyte_conn_id=airbyte_con_id,
        connection_id=connect_id,
    )
sync_source_destination

# # [START howto_operator_airbyte_asynchronous]
# async_source_destination = AirbyteTriggerSyncOperator(
#     task_id="airbyte_async_source_dest_example",
#     connection_id=CONN_ID,
#     asynchronous=True,
# )

# airbyte_sensor = AirbyteJobSensor(
#     task_id="airbyte_sensor_source_dest_example",
#     airbyte_job_id=async_source_destination.output,
# )
# # [END howto_operator_airbyte_asynchronous]

# Task dependency created via `XComArgs`:
