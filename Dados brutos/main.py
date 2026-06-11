import pandas as pd



csv_path = r'Dados brutos\used_car_sales.csv'
# carregar
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')


# Verifica as primeiras linhas
print(df.head())

# Quantidade de linhas e colunas
#print(df.shape)

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
print(df.info())

# transformar datas '01/01/1970' da coluna 'Sold Date' em 'Null'
df['Sold Date'] = df['Sold Date'].replace(pd.to_datetime('01/01/1970'), pd.NaT)

# Quantos valores 'Nat' existem na coluna 'Sold Date'
print(df['Sold Date'].isnull().sum())

# Verificar se existe algum registro onde 'Sold Date' < 'Purchased Date' ignorando os valores 'Nat'
invalid_dates = df[(df['Sold Date'] < df['Purchased Date']) & (df['Sold Date'].notnull()) & (df['Purchased Date'].notnull())]
print(invalid_dates)

# Remover os registros onde 'Sold Date' < 'Purchased Date'
df = df[~((df['Sold Date'] < df['Purchased Date']) & (df['Sold Date'].notnull()) & (df['Purchased Date'].notnull()))]
print(invalid_dates.shape[0])