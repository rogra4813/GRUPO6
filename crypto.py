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
col1.markdown('''**:violet[Input Options]**''')

