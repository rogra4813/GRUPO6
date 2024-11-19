

import streamlit as st
import pandas as pd
import pip

#pip.main(["install"])

st.title('EJERCICIO PRÁCTICO GRUPO 6')
try:
   df = pd.read_excel('cryptos.xlsx')
   st.write()
except FileNotFoundError:
    st.error("El archivo 'cryptos.xlsx' no se encuentra en el directorio.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar el archivo: {e}")

#with open('precios_criptomonedas_incrementales.csv', mode='r') as archivo_csv:
   # lector_csv = csv.reader(archivo_csv)
   # for fila in lector_csv:
       # print(fila)
