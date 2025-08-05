import streamlit as st
import cv2

def apply_negative(image):
    st.sidebar.subheader("Filtro Negativo")

    # Checkbox para ativar/desativar
    use_negative = st.sidebar.checkbox("Aplicar efeito negativo")

    if use_negative:
        # Inversão dos pixels (255 - valor)
        negative = cv2.bitwise_not(image)
        return negative

    return image
