from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.sensors.python import PythonSensor
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.providers.airbyte.hooks.airbyte import AirbyteHook

def create_dag(dag_id, airbyte_conn_id, connection_id, dbt_dir, default_args):
    def check_airbyte_health():
        airbyte_hook = AirbyteHook(airbyte_conn_id=airbyte_conn_id)
        is_healthy, message = airbyte_hook.test_connection()
        print(message)
        return is_healthy

    with DAG(
        dag_id=dag_id,
        default_args=default_args,
        schedule='@daily',
    ) as dag:
        
        start_pipeline_task = EmptyOperator(task_id="start_pipeline")
        end_pipeline_task = EmptyOperator(task_id="end_pipeline")

        airbyte_precheck_task = PythonSensor(
            task_id="check_airbyte_health",
            poke_interval=10,
            timeout=3600,
            mode="poke",
            python_callable=check_airbyte_health,
        )
       
        trigger_airbyte_sync_task = AirbyteTriggerSyncOperator(
            task_id='airbyte_trigger_sync',
            airbyte_conn_id=airbyte_conn_id,
            connection_id=connection_id,
            asynchronous=True
        )

        wait_for_sync_completion_task = AirbyteJobSensor(
            task_id='airbyte_check_sync',
            airbyte_conn_id=airbyte_conn_id,
            airbyte_job_id=trigger_airbyte_sync_task.output
        )

        run_dbt_check_task = BashOperator(
            task_id='run_dbt_precheck',
            bash_command='pwd && dbt debug',
            cwd=dbt_dir
        )

        run_dbt_model_task = BashOperator(
            task_id='run_dbt_model',
            bash_command='dbt run',
            cwd=dbt_dir
        )

        start_pipeline_task >> airbyte_precheck_task >> trigger_airbyte_sync_task \
            >> [run_dbt_check_task, wait_for_sync_completion_task] \
            >> run_dbt_model_task >> end_pipeline_task
    
    return dag
