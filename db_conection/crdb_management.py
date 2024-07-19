import pandas as pd
import sqlalchemy as sa
import cr_db_credentials as cr


# Helper function to read SQL file
def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
# Connection to cadastro (CockroachDB)
st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

# Read and execute query for cadastro
st_query = read_sql_file("db_conection\\query_cadastro.sql")
st_df = pd.read_sql(st_query, st_engine)
print('\n')
print("Data from cadastro:")
# print(st_df.head())
