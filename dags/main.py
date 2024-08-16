import os
import sys
from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etls.csv_to_stg import csv_to_stg
from etls.stg_lgc_ods import stg_lgc_ods
from etls.ods_to_dds import ods_to_dds
from etls.dds_to_pre_dm import dds_to_pre_dm
from etls.pre_dm_to_dm import pre_dm_to_dm


default_args = {
    'owner': 'gena',
    'start_date': datetime(2024, 7, 1)
}

dag = DAG(
    'csv_to_postgres',
    default_args=default_args,
    description='Transfer data from source to ods',
    schedule_interval=None,
    catchup=False,
)

start_dag = EmptyOperator(
    task_id='start_dag',
    dag=dag
)

end_dag = EmptyOperator(
    task_id='end_dag',
    dag=dag
)


csv_inserting_to_stg = PythonOperator(
    task_id = 'csv_to_stg',
    python_callable = csv_to_stg,
    dag = dag
)

stg_inserting_to_ods = PostgresOperator(
    task_id ='stg_lgc_ods',
    sql = stg_lgc_ods,
    dag = dag
)

ods_to_dds = PostgresOperator(
    task_id ='ods_to_dds',
    sql = ods_to_dds,
    dag = dag
)

dds_to_pre_dm = PostgresOperator(
    task_id = 'dds_to_pre_dm',
    sql = dds_to_pre_dm,
    dag = dag
)

pre_dm_to_dm = PostgresOperator(
    task_id = 'pre_dm_to_dm',
    sql = pre_dm_to_dm,
    dag = dag
)

start_dag >> csv_inserting_to_stg >> stg_inserting_to_ods >> ods_to_dds >> pre_dm_to_dm >> end_dag