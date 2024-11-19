import streamlit as st
#from PIL import Image
import pandas as pd
import base64
#import matplotlib.pyplot as plt
import requests

st.title('EJERCICIO PRÁCTICO GRUPO 6')
st.text("*************************************************************************************************************")
st.text("Web scrapping al URL https://es.investing.com/crypto")
# ---------------------------------#
# Información 
expander_bar = st.expander("**About**")
expander_bar.markdown("""
*:orange[Detalles:]* Este ejercicio práctico permite consolidar lo aprendido en Procesos ETL.

*:orange[Integrantes:]* :blue[GRUPO 6]  
""")


