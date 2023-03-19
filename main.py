import streamlit as st
import pandas as pd
import numpy as np
#from altair.examples.pyramid import df#
#from  import df#

file = 'Combustiveis.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(file, encoding='latin-1', sep = ';')


    return df
df = load_data()
st.title("Preço dos combustiveis 2023")
st.markdown(
    """
    Dashboard teste
    """""
)

st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar tabela"):
        st.markdown("### Tabela de dados")
        st.write(df)

