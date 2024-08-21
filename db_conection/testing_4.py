import sqlalchemy as sa
from sqlalchemy.sql import text
import cr_db_credentials as cr
import pandas as pd
import datetime as dt


st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    

query_schema = read_sql_file("db_conection\\query2.sql")

df_schema = pd.read_sql(query_schema, st_engine)
print(df_schema)