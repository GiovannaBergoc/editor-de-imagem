import streamlit as st
import cv2 as cv
from utils.load_image import get_image_input
from utils.display import show_side_by_side
from utils.geometry import apply_geometry
from utils.intensity import apply_intensity
from utils.filters import apply_negative

# Define o layout e o título do app.
st.set_page_config(page_title="Editor de Imagens", layout="wide")
st.title("Editor de Imagens")

#Chama uma função (no load_image.py) para receber uma imagem do usuário, por upload ou webcam.
image = get_image_input()

if image is not None:
    edited_image = image.copy() # Cria uma cópia da imagem original para edição.

    #aplicar as transformações em sequência, cada uma vinda de um módulo.

    edited_image = apply_geometry(edited_image)
    edited_image = apply_intensity(edited_image)
    edited_image = apply_negative(edited_image)

    show_side_by_side(image, edited_image)

    # Campo para digitar o nome do arquivo
    file_name = st.text_input("Nome do arquivo para salvar", value="editada")


    bgr_image = cv.cvtColor(edited_image, cv.COLOR_RGB2BGR)
    is_success, buffer = cv.imencode(".png", bgr_image)

    if is_success:
        st.download_button(
            "Baixar imagem editada",
            data=buffer.tobytes(),
            file_name= f"{file_name}.png",
            mime="image/png"
        )
    else:
        st.error("Erro ao gerar a imagem para download.")
