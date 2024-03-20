# Define the default arguments for the DAG
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

project_dir = "/home/dereck-katuli/Documents/dbt_proj_1/dbt_proj_1"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# Create the DAG with the specified schedule interval
dag = DAG('dbt_dag', default_args=default_args,
          schedule_interval=timedelta(days=1))
# Define the dbt run command as a BashOperator
run_dbt_model = BashOperator(
    task_id='run_dbt_model',
    # Replace 'my_model.sql' with your file name
    bash_command=f"cd {project_dir} && dbt run",
    dag=dag
)
run_dbt_model
