import pandas as pd
import sqlalchemy as sa
import requests
import api_credentials as api
import cr_db_credentials as cr


def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
# Connection to Cockroach DB
# st = cr.cadastro
# st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
# st_engine = sa.create_engine(st_conn_str)

# list of tables
# st_query = read_sql_file("db_conection\\query3.sql")
# st_df = pd.read_sql(st_query, st_engine)

# Connection to API
# Step 1: Make the API request and get the JSON response
response = requests.get(api.base_url1)
data1 = response.json()

df_main = pd.json_normalize(data1, record_path='resultados')

print(df_main)