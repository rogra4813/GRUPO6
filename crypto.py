import streamlit as st
import pandas as pd
from PIL import Image
import base64
import io
import os

st.title('EJERCICIO PRÁCTICO GRUPO 6')
st.text("*************************************************************************************************************")
st.text("Web scrapping al URL https://es.investing.com/crypto")
st.text("Integrantes: Robert Granda, Francisco García, Fabián Quito y Gabriel Salazar")
#try:
#df = pd.read_excel("datos_criptomonedas.csv")
#st.write(df)
#except FileNotFoundError:
    #st.error("El archivo 'cryptos.xlsx' no se encuentra en el directorio.")
#except Exception as e:
    #st.error(f"Ocurrió un error al cargar el archivo: {e}")
# Load the data
def load_data():
    df = pd.read_csv("datos_criptomonedas.csv")
    return df

data = load_data().copy()


