import streamlit as st
import pandas as pd
import sqlite3

# Cria uma conexão com um banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')


df = pd.read_sql_query("SELECT * FROM mercadolivre_itens", conn)

# Fecha a conexão com o banco de dados
conn.close()

st.title('Pesquisa de Mercado - Televisões Smart ')

st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)
# st.write(df)

total_itens = df.shape[0]
col1.metric(label='Número Total de Itens', value=total_itens)

unique_brands = df['name'].nunique()
col2.metric(label='Número de Tipos de Televisão', value=unique_brands)

average_new_price = f"R$ {round(df['new_price'].mean(), 2)}"
col3.metric(label='Preço Médio Novo (R$)', value=average_new_price)

st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4,2])

top_10 = df['name'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10)
col2.write(top_10)