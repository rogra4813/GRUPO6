import streamlit as st
import pandas as pd

import pip
pip.main(["install", "csv.read"])

st.title('EJERCICIO PRÁCTICO GRUPO 6')

df = df.read.csv('precios_criptomonedas_incrementales.csv')

df.wrtite(df)
