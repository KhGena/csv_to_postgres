import os
import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook


def batch_load_csv_to_db(file_path, table_name, conn, batch_size=1000):
    try:
        with conn.begin():
            for chunk in pd.read_csv(file_path, chunksize=batch_size):
                conn.execute(f"TRUNCATE stg.{table_name};")
                chunk.to_sql(table_name, conn, schema='stg', if_exists='append', index=False)
        print(f"Data from {file_path} loaded into {table_name}.")
    except Exception as e:
        print(f"Error occurred while loading data into {table_name}: {e}")
        conn.rollback()
        raise


def csv_to_stg():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(ROOT_DIR, 'source_data')
    csv_files = [os.path.join(DATA_DIR, name) for name in os.listdir(DATA_DIR) if name.endswith('.csv')]
    
    conn_id = 'db'
    pg_hook = PostgresHook(postgres_conn_id=conn_id)
    engine = pg_hook.get_sqlalchemy_engine()

    with engine.connect() as conn:
        for csv_path in csv_files:
            try:
                table_name = os.path.basename(csv_path).rstrip('.csv')
                batch_load_csv_to_db(csv_path, table_name, conn)
            except Exception as e:
                print(f"Failed to process file {csv_path}.")
                print(f"Error: {e}")
                break