import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/foto.jpg")

with col2:
    st.title("Bang Kardi")
    content="""
        Hi, My name is Kardi, Iam a fullstack programmer, right now i learn how to code with Python, hope
        i could be good python programmer
    """
    st.info(content)