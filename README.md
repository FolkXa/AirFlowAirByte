# Airflow setup with Airbyte and DBT

This folder contains the code to setup Airflow with existing Airbyte and DBT.

## Prerequisites

- Docker
- Docker Compose
- PyPi
- Ever run Airbyte (Because it use Airbyte network)
- DBT

## Setup

1. Clone repository 
`git clone https://github.com/FolkXa/AirFlowAirByte.git`
2. Configurate `.env` file by `cp .env.example .env`

    AIRFLOW_AIRBYTE_CONN='...airflow_connection_in_airflow_web...'  (It in Airflow web at admin -> connections)

    AIRBYTE_CONN_ID='...connection_id_in_airbyte...' (connection id in Airbyte web)

    DBT_PROJ_DIR="../dbt_project" << configure dbt local project path

    you can get `AIRFLOW_AIRBYTE_CONN` at this
![alt text](<Screenshot 2567-08-14 at 13.34.24.png>)

3. Run `docker-compose up -d`