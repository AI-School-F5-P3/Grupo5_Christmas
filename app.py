import streamlit as st
from src.pages import menu_generator, postcard_generator, carol_generator
from src.utils import gpt4_utils, dalle_utils,suno_utils

st.set_page_config(page_title="Holiday Helper", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Menu Generator", "Postcard Generator", "Carol Generator"])

if page == "Menu Generator":
    menu_generator.show()
elif page == "Postcard Generator":
    postcard_generator.show()
else:
    carol_generator.show()