import pandas as pd



csv_path = r'Dados brutos\used_car_sales.csv'
# carregar
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')


print("Iniciando ETL...")
print(f"Registros carregados: {df.shape[0]}")

# Quantidade de linhas e colunas
linhas_iniciais = df.shape[0]

# estatísticas descritivas
#print(df.describe())

# verificar valores nulos
#print(df.isnull().sum())

# primeiros valores da coluna 'Sold Date'
print(df['Sold Date'].head())

# transformar a coluna 'Sold Date' e 'Purchased Date' para o formato de data
df['Sold Date'] = pd.to_datetime(df['Sold Date'], format='%d/%m/%Y')
df['Purchased Date'] = pd.to_datetime(df['Purchased Date'], format='%d/%m/%Y')

# Identifica os tipos de dados
print("Tipos de dados:")
print(df.info())

# transformar datas '01/01/1970' da coluna 'Sold Date' em 'Null'
df['Sold Date'] = df['Sold Date'].replace(pd.to_datetime('01/01/1970'), pd.NaT)

# Quantos valores 'Nat' existem na coluna 'Sold Date'
print(f"Valores nulos na coluna 'Sold Date': {df['Sold Date'].isnull().sum()}")

# Verificar se existe algum registro onde 'Sold Date' < 'Purchased Date' ignorando os valores 'Nat'
invalid_dates = df[(df['Sold Date'] < df['Purchased Date']) & (df['Sold Date'].notnull()) & (df['Purchased Date'].notnull())]
print(f"Registros com datas inconsistentes: {invalid_dates.shape[0]}")

# Remover os registros onde 'Sold Date' < 'Purchased Date'
df = df[~((df['Sold Date'] < df['Purchased Date']) & (df['Sold Date'].notnull()) & (df['Purchased Date'].notnull()))]
print(f"Registros removidos por inconsistência de datas: {invalid_dates.shape[0]}")

# Criando novas colunas 'Profit', 'Vehicle Age' e 'Sale Year'
df['Profit'] =  df['Purchased Price-$'] - df['Sold Price-$'] 
df['Vehicle Age'] = df['Purchased Date'].dt.year - df['Manufactured Year']
df['Sale Year'] = df['Sold Date'].dt.year

# Verificar as primeiras linhas do DataFrame atualizado
print("Primeiras linhas do DataFrame atualizado:")
print(df.head())

# exibindo as colunas do DataFrame
print("Colunas do DataFrame:")
print(df.columns.tolist())

# Verificar a quantidade de registros e colunas após as transformações
linhas_finais = df.shape[0]
print(f"Registros após ETL: {df.shape[0]}")

# Salvando o DataFrame atualizado em um novo arquivo CSV
output_csv_path = r'Dados Tratados\used_car_sales_gold.csv'

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv(output_csv_path, index=False, sep=';', encoding='utf-8')

print(output_csv_path)