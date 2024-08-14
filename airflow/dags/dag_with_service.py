# from services.airflow_airbyte_automate import create_dag
# from datetime import timedelta
# import pendulum

# AIRFLOW_AIRBYTE_CONN_ID = 'LocalAirByte' # The name of the Airflow connection to get connection information for Airbyte.
# AIRBYTE_CONNECTION_ID = '1a43757a-d971-49b8-b5f4-30a36413cba3' # the Airbyte ConnectionId UUID between a source and destination.
# DBT_DIR = "/opt/airflow/dbt_project" # the dbt Path in docker

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': pendulum.today('UTC').add(days=-1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag1 = create_dag(dag_id='DAG1', 
#            airbyte_conn_id=AIRFLOW_AIRBYTE_CONN_ID, 
#            connection_id=AIRBYTE_CONNECTION_ID, 
#            dbt_dir=DBT_DIR, 
#            default_args=default_args)

# dag2 = create_dag(dag_id='DAG2', 
#            airbyte_conn_id=AIRFLOW_AIRBYTE_CONN_ID, 
#            connection_id=AIRBYTE_CONNECTION_ID, 
#            dbt_dir=DBT_DIR, 
#            default_args=default_args)