import pandas as pd



csv_path = r'Dados brutos\used_car_sales.csv'
# carregar
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')


# Verifica as primeiras linhas

# Quantidade de linhas e colunas
print(df.shape)

# Indentofica os tipos de dados
print(df.info())

# estatísticas descritivas
print(df.describe())

# verificar valores nulos
print(df.isnull().sum())




