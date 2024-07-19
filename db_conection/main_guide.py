import pandas as pd
import sqlalchemy as sa
import cr_db_credentials as cr

# Helper function to read SQL file
def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

# Connection to data_warehouse (PostgreSQL)
# dw = cr.data_warehouse
# dw_conn_str = f"postgresql://{dw['u_name']}:{dw['passwd']}@{dw['host']}:{dw['port']}/{dw['db_name']}"
# dw_engine = sa.create_engine(dw_conn_str)

# # Read and execute query for data_warehouse
# dw_query = read_sql_file("db_conection\\query1.sql")
# dw_df = pd.read_sql(dw_query, dw_engine)
# print("Data from data_warehouse:")
# print(dw_df.head())


# Connection to cadastro (CockroachDB)
st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

# Read and execute query for cadastro
st_query = read_sql_file("db_conection\\query2.sql")
st_df = pd.read_sql(st_query, st_engine)
print("Data from cadastro:")
print(st_df.head())
