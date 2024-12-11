import streamlit as st
from utils.gpt4_utils import generate_recipes

def show():
    st.title("Generate Recipes")

    prompt = st.text_area("Describe the diners' characteristics (allergens, ages, budget, types of cuisine):")

    if st.button("Generate Menu"):
        if prompt:
            recipes = generate_recipes(prompt)
            st.write(recipes)
        else:
            st.error("Please enter a prompt.")

        