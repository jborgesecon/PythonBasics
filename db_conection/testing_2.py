import pandas as pd
import sqlalchemy as sa
from datetime import datetime
import cr_db_credentials as cr

# Helper function to read SQL file
def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def drop_schema(schema_name):
    drop_query = f"DROP SCHEMA IF EXISTS {schema_name} CASCADE"
    with st_engine.connect() as conn:
        conn.execute(sa.text(drop_query))
    print(f"Schema {schema_name} dropped.")


# Establish connection with cockroachdb
st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

query_schema = read_sql_file("db_conection\\query1.sql")
# query_tables = read_sql_file("db_conection\\query2.sql")
# query_views = read_sql_file("db_conection\\query3.sql")
# query_drop = read_sql_file("db_conection\\query4.sql")


df_schema = pd.read_sql(query_schema, st_engine)
# df_tables = pd.read_sql(query_tables, st_engine)
# df_views = pd.read_sql(query_views, st_engine)

# print("Schema:")
# print(df_schema)

# print("Tables:")
# print(df_tables)

# print("Views:")
# print(df_views)


# with st_engine.connect() as connection:
#     try:
#         connection.execute(sa.text(query_drop))
#         drop_schema("cadastro")
#         print("Schema dropped successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

print('\n')
df_schema = pd.read_sql(query_schema, st_engine)
print(df_schema)



# Read and execute query for cadastro
# st_query = read_sql_file("db_conection\\query2.sql")
# st_df = pd.read_sql(st_query, st_engine)
# print("Data from cadastro:")
# print(st_df.head())
