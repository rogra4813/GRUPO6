import streamlit as st
#from PIL import Image
import pandas as pd
import base64
#import matplotlib.pyplot as plt
import requests

st.title('EJERCICIO PRÁCTICO ETL')
st.text("*************************************************************************************************************")

# ---------------------------------#
# Información 
expander_bar = st.expander("**Más sobre este trabajo**")
expander_bar.markdown("""
*:orange[Información:]* Este ejercicio práctico permite consolidar lo aprendido en Diseños de procesos ETL en Data Science, para ello, serecurrió a realizar un web scrapping a la URL https://es.investing.com/crypto/bitcoin, para extraer la información de las cryptos.

*:orange[Integrantes:]* :blue[GRUPO 6]  
""")

# Enter your CoinMarketCap API key here
api_key = '58c2d26e-6b17-4a26-933b-625fef84e704'  # Replace with your actual API key

# Make API requests to CoinMarketCap
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

