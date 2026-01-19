import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
from PIL import Image, ImageOps

model = keras.models.load_model("/models/zalando.keras")

st.title("Ialando - Clasificación de prendas")

uploaded_files = st.file_uploader(
    "Sube una imagen de la prenda que quieres clasificar", accept_multiple_files="directory", type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    # Carga y procesa la imagen
    image = Image.Open(uploaded_files).convert("L") # Escala de grises
    image = ImageOps.invert(image) # Invierte la imagen
    image = image.resize((28, 28)) # Redimensiona
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

    # Prediccion
    prediction = model.predict(img_array)
    predicted_class = class_name[np.argmax(prediction)]

    st.write(f"Vector de prediccion: ${prediction}")
    st.write(f"La prenda es: ${predicted_class}")

