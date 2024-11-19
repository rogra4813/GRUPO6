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

# ---------------------------------#
# Page layout (continued)
## Divide page into 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3 = st.columns((2, 1))

# ---------------------------------#
# Sidebar + Main panel
col1.markdown('''**:violet[Opciones de entrada]**''')

## Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

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

# Make the API request
    response = requests.get(api_url, params=params, headers=headers)

    # Parse the JSON response
    data = response.json()

    # Extract cryptocurrency data
    cryptocurrencies = data['data']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    for crypto in cryptocurrencies:
        coin_name.append(crypto['name'])
        coin_symbol.append(crypto['symbol'])
        price.append(crypto['quote'][currency_price_unit]['price'])
        percent_change_1h.append(crypto['quote'][currency_price_unit]['percent_change_1h'])
        percent_change_24h.append(crypto['quote'][currency_price_unit]['percent_change_24h'])
        percent_change_7d.append(crypto['quote'][currency_price_unit]['percent_change_7d'])
        market_cap.append(crypto['quote'][currency_price_unit]['market_cap'])
        volume_24h.append(crypto['quote'][currency_price_unit]['volume_24h'])

    df = pd.DataFrame(
        columns=['coin_name', 'coin_symbol', 'marketCap', 'percentChange1h', 'percentChange24h', 'percentChange7d',
                 'price', 'volume24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['percentChange1h'] = percent_change_1h
    df['percentChange24h'] = percent_change_24h
    df['percentChange7d'] = percent_change_7d
    df['marketCap'] = market_cap
    df['volume24h'] = volume_24h

    return df

df = load_data()
