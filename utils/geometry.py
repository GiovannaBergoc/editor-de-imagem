import streamlit as st
import cv2
import numpy as np

def apply_geometry(image):
    st.sidebar.subheader("Transformações Geométricas")

    # Rotação
    angle = st.sidebar.slider("Rotação (graus)", -180, 180, 0)

    # Escala
    scale = st.sidebar.slider("Escala", 10, 300, 100) / 100.0  # de 0.1 a 3.0

    # Cisalhamento
    shear_x = st.sidebar.slider("Cisalhamento Horizontal", -100, 100, 0) / 100.0
    shear_y = st.sidebar.slider("Cisalhamento Vertical", -100, 100, 0) / 100.0

    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)

    # Matriz de rotação + escala
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Adiciona cisalhamento (como extensão da matriz 2x3)
    shear_matrix = np.float32([
        [1, shear_x, 0],
        [shear_y, 1, 0]
    ])

    # Aplica rotação e escala
    rotated_scaled = cv2.warpAffine(image, rotation_matrix, (cols, rows))

    # Aplica cisalhamento
    transformed = cv2.warpAffine(rotated_scaled, shear_matrix, (cols, rows))

    return transformed
