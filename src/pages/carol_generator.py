import streamlit as st
from utils.suno_utils import generate_carol

def show():
    st.title("Generate Christmas Carol")

    description = st.text_area("Describe the carol:")
    details = st.text_area("Specific details:")
    music_type = st.text_input("Type of music:")

    if st.button("Generate Carol"):
        if description and details and music_type:
            carol = generate_carol(description, details, music_type)
            st.write(carol)
        else:
            st.error("Please fill in all fields.")