pimport streamlit as st
import pandas as pd

st.title('EJERCICIO PRÁCTICO GRUPO 6')
try:
   df = pd.read_excel('Presupuesto personal1.xlsx')
   st.write(df)
except FileNotFoundError:
    st.error("El archivo 'cryptos.xlsx' no se encuentra en el directorio.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar el archivo: {e}")

