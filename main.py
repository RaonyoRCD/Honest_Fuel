import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import tkinter
file = 'Banco de Dados/Dados.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(file, encoding='latin-1', sep = ';')

    return df
df = load_data()

image = Image.open('Fotos/univesp.png')

with st.columns(3)[1]:
    st.image(image, use_column_width='auto')

st.title("Honest Fuel – Análises de Preços de Combustíveis")

# Row A
a1, a2, a3, a4, a5 = st.columns(5)
a2.metric("Gasolina", "+0,23", "10%")
a3.metric("Etanol", "+0,12", "7%")
a4.metric("Diesel", "+0,18", "9%")
a5.metric("GNV", "-0,10", "-5%")

# Row B
#b1, b2, b3, b4 = st.columns(4)
#b1.metric("Temperature", "70 °F", "1.2 °F")
#b2.metric("Wind", "9 mph", "-8%")
#b3.metric("Humidity", "86%", "4%")
#b4.metric("Humidity", "86%", "4%")


st.markdown(
    """
    :bar_chart: Dashboard
    """""
)

st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar tabela"):
        st.markdown("### Tabela de dados")
        st.write(df)

# ---- SIDEBAR ----
customer_type = st.sidebar.multiselect(
    "Selecione o combustivel:",
    options=df["Produto"].unique(),
    #default=df["Produto"].unique(),
)

gender = st.sidebar.multiselect(
    "Selecione a unidade de medida:",
    options=df["Unidade_de_Medida"].unique(),
    #default=df["Unidade_de_Medida"].unique()
)

city = st.sidebar.multiselect(
  "Selecio o municipio:",
   options=df["Municipio"].unique(),
   #default=df["Municipio"].unique()
)

df_selection = df.query(
    "Municipio == @city & Produto ==@customer_type & Unidade_de_Medida == @gender"
)

chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['Gasolina', 'Etanol', 'Diesel', 'GNV'])

st.bar_chart(df, y='Produto', x='Valor_de_Venda')

st.line_chart(chart_data)

st.bar_chart(chart_data)

names = ['Gasolina', 'Etanol', 'GNV', 'Diesel']
size = [30, 11, 3, 12]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Custom wedges
plt.pie(size, labels=names, wedgeprops={'linewidth': 7})
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig("teste.png")

image2 = Image.open('teste.png')
with st.columns(3)[1]:
    st.image(image2, use_column_width='auto')

# Convertendo a coluna "data" para o formato de data
df["Data_da_Coleta"] = pd.to_datetime(df["Data_da_Coleta"])

# Criando o gráfico de linhas com data, tipo de produto e valor
fig = px.bar(df, x="Data_da_Coleta", y="Valor_de_Venda", color="Produto", title="Vendas por tipo de produto")

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)