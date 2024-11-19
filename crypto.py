import streamlit as st
#from PIL import Image
import pandas as pd
import base64
#import matplotlib.pyplot as plt
import requests

st.title('EJERCICIO PRÁCTICO GRUPO 6')
st.text("*************************************************************************************************************")

# ---------------------------------#
# Información 
expander_bar = st.expander("**Más sobre este trabajo**")
expander_bar.markdown("""
*:orange[Información:]* Este ejercicio práctico permite consolidar lo aprendido en Diseños de procesos ETL en Data Science, para ello, serecurrió a realizar un web scrapping a la URL https://es.investing.com/crypto/bitcoin, para extraer la información de las cryptos.

*:orange[Integrantes:]* :blue[GRUPO 6]  
""")


