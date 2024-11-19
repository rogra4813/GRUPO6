import streamlit as st
import pandas as pd

#import pip
#pip.main(["install", "openpyxl"])

st.title('EJERCICIO PRÁCTICO GRUPO 6')

#df = df.read_csv('precios_criptomonedas_incrementales.csv')

#df.wrtite(df)

with open('precios_criptomonedas_incrementales.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
