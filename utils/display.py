import streamlit as st

def show_side_by_side(original, edited):
    st.subheader("Visualização lado a lado")

    col1, col2 = st.columns(2)

    with col1:
        st.image(original, caption="Original", use_container_width=True)
    with col2:
        st.image(edited, caption="Editada", use_container_width=True)
