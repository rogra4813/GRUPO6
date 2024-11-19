import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import requests

#st.title('EJERCICIO PRÁCTICO GRUPO 6')
#st.text("*************************************************************************************************************")
#st.text("Web scrapping al URL https://es.investing.com/crypto")
#st.text("Integrantes: Robert Granda, Francisco García, Fabián Quito y Gabriel Salazar")
#try:
#df = pd.read_excel("datos_criptomonedas.csv")
#st.write(df)
#except FileNotFoundError:
    #st.error("El archivo 'cryptos.xlsx' no se encuentra en el directorio.")
#except Exception as e:
    #st.error(f"Ocurrió un error al cargar el archivo: {e}")

st.header('Crypto Price App', divider='rainbow')
st.subheader(
    ':rainbow[This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**! ] ')

def load_data():
    # Define the API URL
    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    # Define the parameters for the API request
    params = {
        'start': '1',
        'limit': '100',
        'convert': currency_price_unit  # Use the selected currency unit
    }

    # Set the API key in the headers
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }

