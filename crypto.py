import streamlit as st
import pandas as pd
from PIL import Image
import base64
import io
import os

#st.title('EJERCICIO PRÁCTICO GRUPO 6')
#st.text("*************************************************************************************************************")
#st.text("Web scrapping al URL https://es.investing.com/crypto")
#st.text("Integrantes: Robert Granda, Francisco García, Fabián Quito y Gabriel Salazar")
#try:
#df = pd.read_excel("datos_criptomonedas.csv")
#st.write(df)
#except FileNotFoundError:
    #st.error("El archivo 'cryptos.xlsx' no se encuentra en el directorio.")
#except Exception as e:
    #st.error(f"Ocurrió un error al cargar el archivo: {e}")

st.markdown("<h1 style='text-align: center;'>EJERCICIO PRÁCTICO 3</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; '>GRUPO 6 </p>", unsafe_allow_html=True)
st.write("")
# Load the data
def load_data():
    df = pd.read_csv("datos_criptomonedas.csv")
    return df

data = load_data().copy()

# Convert image to Base64
def image_to_base64(img_path, output_size=(64, 64)):
    # Check if the image path exists
    if os.path.exists(img_path):
        with Image.open(img_path) as img:
            img = img.resize(output_size)
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            return f"data:image/png;base64,{base64.b64encode(buffered.getvalue()).decode()}"
    return ""


