# utils/load_image.py
import streamlit as st
import cv2 
import numpy as np
from PIL import Image

def get_image_input():
    st.sidebar.header("Entrada da Imagem") #Adiciona um título na barra lateral da interface do Streamlit

    option = st.sidebar.radio("Selecione a fonte da imagem:", ("Upload", "Webcam"))

    if option == "Upload":
        uploaded_file = st.sidebar.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            return np.array(image)

    elif option == "Webcam":
        picture = st.sidebar.camera_input("Tirar foto")
        if picture is not None:
            image = Image.open(picture).convert("RGB")
            return np.array(image)

    return None
