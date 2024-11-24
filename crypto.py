

import streamlit as st
#from PIL import Image
import pandas as pd
import base64
#import matplotlib.pyplot  as plt
import requests


st.title('EXAMEN FINAL DISEÑO DE PROCESOS  ETL')
st.text("*************************************************************************************************************")

# ---------------------------------#
# Información 
expander_bar = st.expander("**Más sobre este trabajo**")
expander_bar.markdown("""
*:orange[Información:]* Este ejercicio práctico permite consolidar lo aprendido en Diseños de procesos ETL en Data Science, para ello, se realizó un web scrapping a la URL https://es.investing.com/crypto/bitcoin, para extraer la información de las cryptos.

*:orange[Integrantes:]* :blue[GRUPO 6]  
""")

# ---------------------------------#
# Page layout (continued)
## Divide page into 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2 = st.container()  

# ---------------------------------#
# Sidebar + Main panel
col1.markdown('''**:violet[Opciones de entrada]**''')

### Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Selecccione la modena', ('USD'))

# Enter your CoinMarketCap API key here
api_key = '58c2d26e-6b17-4a26-933b-625fef84e704'  # Replace with your actual API key

# Make API requests to CoinMarketCap
def load_data():
    # Define the API URL
    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    # Define the parameters for the API request
    params = {
        'start': '1',
        'limit': '10',
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

    Nombre = []
    Símbolo = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    PrecioUSD = []
    volume_24h = []

    for crypto in cryptocurrencies:
        Nombre.append(crypto['name'])
        Símbolo.append(crypto['symbol'])
        PrecioUSD.append(crypto['quote'][currency_price_unit]['price'])
        percent_change_1h.append(crypto['quote'][currency_price_unit]['percent_change_1h'])
        percent_change_24h.append(crypto['quote'][currency_price_unit]['percent_change_24h'])
        percent_change_7d.append(crypto['quote'][currency_price_unit]['percent_change_7d'])
        market_cap.append(crypto['quote'][currency_price_unit]['market_cap'])
        volume_24h.append(crypto['quote'][currency_price_unit]['volume_24h'])

    df = pd.DataFrame(
        columns=['Nombre', 'Símbolo', 'PrecioUSD', 'marketCap', 'percentChange1h', 'percentChange24h', 'percentChange7d',
                 'volume24h'])
    df['Nombre'] = Nombre
    df['Símbolo'] = Símbolo
    df['PrecioUSD'] = PrecioUSD
    df['percentChange1h'] = percent_change_1h
    df['percentChange24h'] = percent_change_24h
    df['percentChange7d'] = percent_change_7d
    df['marketCap'] = market_cap
    df['volume24h'] = volume_24h

    return df

df = load_data()

## Sidebar - Cryptocurrency selections
sorted_coin = sorted(df['Símbolo'])
selected_coin = col1.multiselect('Criptomonedas', sorted_coin, sorted_coin)

df_selected_coin = df[df['Símbolo'].isin(selected_coin)]  # Filtering data

## Sidebar - Number of coins to display
num_coin = col1.slider('Desplegar el número de criptos', 1, 10, 10)
df_coins = df_selected_coin[:num_coin]



## Sidebar - Sorting values
sort_values = col1.selectbox('Ordenar?', ['Si', 'No'])

col2.subheader('10 CRIPTOMONEDAS MÁS POPULARES')
col2.dataframe(df_coins)

# ---------------------------------#
# Gráfica de precios de criptomonedas seleccionadas en el contenedor principal (col2)
with col2:
    if not df_coins.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(df_coins['Nombre'], df_coins['PrecioUSD'], color='blue')
        plt.xlabel('Criptomonedas')
        plt.ylabel(f'Precio en {currency_price_unit}')
        plt.title('Precios de Criptomonedas Seleccionadas')
        plt.xticks(rotation=45)
        
        # Mostrar la gráfica en Streamlit
        st.pyplot(plt)
