# Importa as bibliotecas necessárias
import pandas as pd
import sqlite3
from datetime import datetime

# Carrega os dados de um arquivo JSON para um DataFrame do pandas
df = pd.read_json('C:\\Users\\Ítalo Monteiro\\OneDrive\\Desktop\\Scraping\\data\\data.json')

# Adiciona uma nova coluna '_source' contendo a URL de onde os dados foram coletados
df['_source'] = "https://lista.mercadolivre.com.br/televisao-smart#D[A:televisao%20smart]"

# Adiciona uma nova coluna '_data_coleta' com a data e hora atual, indicando quando os dados foram coletados
df['_data_coleta'] = datetime.now()

# Trata valores nulos nas colunas de preço antigo e novo (em reais e centavos)
# Substitui valores nulos por 0 e converte os dados para o tipo float
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)

# Trata valores nulos na coluna 'reviews_rating_number', substituindo nulos por 0 e convertendo para float
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remove parênteses dos valores na coluna 'reviews_amount' e converte os dados para inteiros
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace(r'[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Cria uma nova coluna 'old_price' calculando o preço antigo a partir de reais e centavos
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100

# Cria uma nova coluna 'new_price' calculando o novo preço a partir de reais e centavos
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remove as colunas desnecessárias de preço em reais e centavos após a criação das colunas agregadas 'old_price' e 'new_price'
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# Cria uma conexão com um banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')

# Salva o DataFrame em uma tabela SQL chamada 'mercadolivre_items' no banco de dados, substituindo os dados se a tabela já existir
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fecha a conexão com o banco de dados
conn.close()
