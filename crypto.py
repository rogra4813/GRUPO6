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
#def image_to_base64(img_path, output_size=(64, 64)):
    # Check if the image path exists
    #if os.path.exists(img_path):
        #with Image.open(img_path) as img:
            #img = img.resize(output_size)
            #buffered = io.BytesIO()
            #img.save(buffered, format="PNG")
            #return f"data:image/png;base64,{base64.b64encode(buffered.getvalue()).decode()}"
    #return ""
# If 'Logo' column doesn't exist, create one with path to the logos
#if 'Logo' not in data.columns:
    #output_dir = 'downloaded_logos'
    #data['Logo'] = data['Name'].apply(lambda name: os.path.join(output_dir, f'{name}.png'))

# Convert image paths to Base64
#data["Logo"] = data["Logo"].apply(image_to_base64)

#image_column = st.column_config.ImageColumn(label="")
nombre_column = st.column_config.TextColumn(label="Nombre")
simbolo_column = st.column_config.TextColumn(label="Símbolo")
precio_column = st.column_config.TextColumn(label="Precio USD.")

# Adjust the index to start from 1 and display only the first 25 companies
data.reset_index(drop=True, inplace=True)
data = data.head(25)
data.index = data.index + 1

data = data[['Nombre', 'Símbolo', 'Precio USD.']]


# Display the dataframe
st.dataframe(data, height=913, column_config={"Nombre":nombre_column,'Símbolo':simbolo_column,'Precio USD.':precio_column})

import datetime

# Získání aktuálního data
dnesni_datum = datetime.date.today().strftime("%d.%m.%Y")  # Formátování data na formát DD.MM.YYYY

#st.markdown(f'<span style="font-size: 14px">**Zdroj:** companiesmarketcap.com | **Data:** k {dnesni_datum} | **Autor:** lig </span>', unsafe_allow_html=True)

