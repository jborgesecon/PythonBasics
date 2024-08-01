import pandas as pd
import sqlalchemy as sa
import requests
import api_credentials as api
import cr_db_credentials as cr


def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
# Connection to Cockroach DB
st = cr.cadastro
st_conn_str = f"cockroachdb://{st['u_name']}:{st['passwd']}@{st['host']}:{st['port']}/{st['db_name']}"
st_engine = sa.create_engine(st_conn_str)

# list of tables
st_query = read_sql_file("db_conection\\query3.sql")
st_df = pd.read_sql(st_query, st_engine)
# print("Data from cadastro:")
# print(st_df)

# Connection to API
# Step 1: Make the API request and get the JSON response
response = requests.get(api.base_url1)
data1 = response.json()

# {
#     "id": "355",
#     "variavel": "IPCA15 - Variação mensal",
#     "unidade": "%",
#     "resultados": [
#         {
#             "classificacoes": [
#                 {
#                     "id": "315",
#                     "nome": "Geral, grupo, subgrupo, item e subitem",
#                     "categoria": {
#                         "7169": "Índice geral"
#                     }
#                 }
#             ],
#             "series": [
#                 {
#                     "localidade": {
#                         "id": "3501",
#                         "nivel": {
#                             "id": "N7",
#                             "nome": "Região Metropolitana"
#                         },
#                         "nome": "São Paulo (SP)"
#                     },
#                     "serie": {
#                         "201908": "0.31",
#                         "201909": "0.19",
#                         "201910": "0.06",
#                         "201911": "0.29",
#                         "201912": "0.88",
#                         "202001": "0.90"
#                     }
#                 },
#                 {
#                     "localidade": {
#                         "id": "3301",
#                         "nivel": {
#                             "id": "N7",
#                             "nome": "Região Metropolitana"
#                         },
#                         "nome": "Rio de Janeiro (RJ)"
#                     },
#                     "serie": {
#                         "201908": "-0.13",
#                         "201909": "-0.10",
#                         "201910": "0.18",
#                         "201911": "0.11",
#                         "201912": "0.97",
#                         "202001": "0.47"
#                     }
#                 }
#             ]
#         }
#     ]
# }

# Extracting the relevant part of the JSON
all_series = pd.DataFrame()
for i in range(len(data1)):
    resultados = data1[i]['resultados']

    # Initialize an empty DataFrame to store all series data

    # Loop through each 'resultados' item
    for resultado in resultados:
        classificacoes = resultado['classificacoes']
        series = resultado['series']
        
        # Loop through each 'series' item
        for serie in series:
            localidade = serie['localidade']
            localidade_nivel = localidade['nivel']
            
            # Flatten the 'serie' dictionary into a DataFrame
            df = pd.DataFrame.from_dict(serie['serie'], orient='index', columns=['value'])
            df['date'] = df.index
            df['localidade_id'] = localidade['id']
            df['localidade_nome'] = localidade['nome']
            df['localidade_nivel_id'] = localidade_nivel['id']
            df['localidade_nivel_nome'] = localidade_nivel['nome']
            df['classificacoes_id'] = classificacoes[0]['id']
            df['classificacoes_nome'] = classificacoes[0]['nome']
            df['categoria'] = list(classificacoes[0]['categoria'].values())[0]
            
            # Append metadata
            df['id'] = data1[i]['id']
            df['variavel'] = data1[i]['variavel']
            df['unidade'] = data1[i]['unidade']
            
            # Append to the main DataFrame
            all_series = pd.concat([all_series, df], ignore_index=True)

# Reset index
all_series.reset_index(drop=True, inplace=True)

# Print the cleaned DataFrame
# print(all_series.columns)
for n in all_series.columns:
    print(n)
    # print('\n')

# export as csv
all_series.to_csv(".\\data1.csv", index=False)