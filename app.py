import streamlit as st
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent / 'src'))

from pages import menu_generator, postcard_generator, carol_generator
from utils import gpt4_utils, dalle_utils, suno_utils

st.set_page_config(page_title="Holiday Helper", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Menu Generator", "Postcard Generator", "Carol Generator"])

if page == "Menu Generator":
    menu_generator.show()
elif page == "Postcard Generator":
    postcard_generator.show()
else:
    carol_generator.show()