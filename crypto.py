import streamlit as st
import pandas as pd
import pip

pip.main(["install"])

st.title('EJERCICIO PRÁCTICO GRUPO 6')

df = pd.read_excel('cryptos.xlsx')

st.write(df)

#with open('precios_criptomonedas_incrementales.csv', mode='r') as archivo_csv:
   # lector_csv = csv.reader(archivo_csv)
   # for fila in lector_csv:
       # print(fila)
