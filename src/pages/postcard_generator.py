import streamlit as st
from utils.dalle_utils import generate_postcard
from utils.gpt4_utils import generate_email_text

def show():
    st.title("Create Christmas Postcard")

    prompt = st.text_area("Describe the type of image for the Christmas postcard:")

    if st.button("Generate Postcard"):
        if prompt:
            postcard_url = generate_postcard(prompt)
            st.image(postcard_url, caption="Generated Postcard")
            
            email_text = generate_email_text(prompt)
            st.write("Email Text:")
            st.write(email_text)
        else:
            st.error("Please enter a prompt.")