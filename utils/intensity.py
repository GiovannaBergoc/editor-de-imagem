import streamlit as st
import cv2
import numpy as np

def apply_intensity(image):
    st.sidebar.subheader("Ajustes de Intensidade")

    # Brilho
    brightness = st.sidebar.slider("Brilho", -100, 100, 0)

    # Contraste
    contrast = st.sidebar.slider("Contraste", -100, 100, 0)

    # Tipo de transformação
    transform_type = st.sidebar.radio("Transformação personalizada:", ["Nenhuma", "Logarítmica", "Gama"])

    # Aplica brilho e contraste
    img = cv2.convertScaleAbs(image, alpha=1 + (contrast / 100), beta=brightness)

    # Aplica transformação personalizada
    if transform_type == "Logarítmica":
        img_float = np.float32(img) + 1.0
        img_log = cv2.normalize(cv2.log(img_float), None, 0, 255, cv2.NORM_MINMAX)
        img = np.uint8(img_log)

    elif transform_type == "Gama":
        gamma = st.sidebar.slider("Gama", 0.1, 5.0, 1.0)
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)]).astype("uint8")
        img = cv2.LUT(img, table)

    return img
