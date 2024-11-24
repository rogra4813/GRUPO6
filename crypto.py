import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go  # Importar Plotly para gráficos

st.title('EXAMEN FINAL DISEÑO DE PROCESOS ETL')
st.text("*************************************************************************************************************")

# ---------------------------------#
# Información 
expander_bar = st.expander("**Más sobre este trabajo**")
expander_bar.markdown("""
*:orange[Información:]* Este ejercicio práctico permite consolidar lo aprendido en Diseños de procesos ETL en Data Science, para ello, se realizó un web scrapping, para extraer la información de las cryptos.

*:orange[Integrantes:]* :blue[GRUPO 6]  
""")

# ---------------------------------#
# Page layout
col1 = st.sidebar
col2 = st.container()  

# ---------------------------------#
# Sidebar + Main panel
col1.markdown('''**:violet[Opciones de entrada]**''')

### Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Seleccione la moneda', ('USD'))

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
# Gráfica de velas japonesas en el contenedor principal (col2)
with col2:
    if not df_coins.empty:
        # Para crear un gráfico de velas japonesas, necesitamos datos adicionales.
        # Asegúrate de tener columnas como 'open', 'high', 'low', y 'close'.
        
        # Suponiendo que tienes esos datos en tu DataFrame (esto es solo un ejemplo):
        # Aquí deberías tener los datos reales para el gráfico de velas.
        
        # Ejemplo de datos ficticios (deberías reemplazar esto con tus datos reales)
        open_prices = [100, 105, 102]
        high_prices = [110, 108, 107]
        low_prices = [95, 100, 101]
        close_prices = [105, 102, 106]
        
        fig = go.Figure(data=[go.Candlestick(x=df_coins['Nombre'],
                                              open=open_prices,
                                              high=high_prices,
                                              low=low_prices,
                                              close=close_prices)])
        
        fig.update_layout(title='Gráfico de Velas Japonesas',
                          xaxis_title='Criptomonedas',
                          yaxis_title='Precio (USD)')
        
        # Mostrar la gráfica en Streamlit
        st.plotly_chart(fig)
