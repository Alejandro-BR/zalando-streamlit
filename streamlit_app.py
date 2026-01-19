import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
from PIL import Image, ImageOps

model = keras.models.load_model("models/zalando.keras")

st.title("Ialando - Clasificación de prendas")

uploaded_files = st.file_uploader(
    "Sube una imagen de la prenda que quieres clasificar",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Carga y procesa la imagen
        image = Image.open(uploaded_file).convert("L")  # Escala de grises
        image = ImageOps.invert(image)  # Invierte la imagen
        image = image.resize((28, 28))  # Redimensiona
        image = ImageOps.autocontrast(image)
        st.image(image, caption="Imagen procesada")

        # Convierte la imagen en un array normalizado
        img_array = np.array(image, dtype=np.float32) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        class_name = [
            "T-shirt/top",
            "Trouser",
            "Pullover",
            "Dress",
            "Coat",
            "Shirt",
            "Sneaker",
            "Bag",
            "Ankle boot"
        ]

        # Predicción
        prediction = model.predict(img_array)
        predicted_class = class_name[np.argmax(prediction)]

        st.write("Vector de predicción:", prediction)
        st.write("La prenda es:", predicted_class)
