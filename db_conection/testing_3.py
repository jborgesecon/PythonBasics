# pyinstaller

import sqlalchemy as sa
from sqlalchemy.sql import text
import cr_db_credentials as cr
import pandas as pd
import datetime as dt


# Replace with your actual connection string
st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

# data = pd.read_csv("db_conection\\dados.csv")

# create new age based on date_of_birth
# data['date_of_birth'] = pd.to_datetime(data['date_of_birth'])
# data['age'] = dt.datetime.now().year - data['date_of_birth'].dt.year


# data.to_sql('dados2', st_engine, schema='classic', if_exists='replace', index=False)

def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

# def drop_schema():
#     with st_engine.connect().execution_options(autocommit = True) as conn:
#         with open("db_conection\\query4.sql", 'r') as query:

#             result = conn.execute(text(query))
#             result2 = pd.DataFrame(result.fetchall())
#     return result2

# def drop_schema(schema_name):
#     drop_query = f"DROP SCHEMA IF EXISTS {schema_name} CASCADE"
#     with st_engine.connect() as conn:
#         conn.execute(sa.text(drop_query))
#     print(f"Schema {schema_name} dropped.")

# drop_schema('raw_datasets')
query_schema = read_sql_file("db_conection\\query2.sql")

# check schemas
df_schema = pd.read_sql(query_schema, st_engine)
print(df_schema)