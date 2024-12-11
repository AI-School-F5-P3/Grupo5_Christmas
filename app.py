import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = "2024-10-21"

st.title("Azure OpenAI with Streamlit")

st.header("Generate Recipes")
recipe_prompt = st.text_input("Enter characteristics for the menu:")
if st.button("Generate Recipes"):
    if recipe_prompt:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates recipes."},
                {"role": "user", "content": recipe_prompt}
            ],
            max_tokens=500
        )
        recipes = response.choices[0].message['content'].strip()
        st.text_area("Generated Recipes", recipes, height=200)
    else:
        st.error("Please enter a prompt for the menu.")

st.header("Generate Email Text for Christmas Postcard")
email_prompt = st.text_input("Enter prompt for the Christmas postcard:")
if st.button("Generate Email Text"):
    if email_prompt:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates email text for Christmas postcards."},
                {"role": "user", "content": email_prompt}
            ],
            max_tokens=500
        )
        email_text = response.choices[0].message['content'].strip()
        st.text_area("Generated Email Text", email_text, height=100)
    else:
        st.error("Please enter a prompt for the email text.")

st.header("Write a Letter to Santa Claus")
name = st.text_input("Your Name:")
age = st.number_input("Your Age:", min_value=0, step=1)
behavior = st.selectbox("How have you been this year?", ["Very Good", "Good", "Okay", "Not So Good", "Bad"])
letter_content = st.text_area("Write your letter here:")

if st.button("Send Letter"):
    if name and age and letter_content:
        system_prompt = "You are Santa Claus, a friendly, kind and cool figure who responds warmly to children's letters."
        user_prompt = f"Dear Santa Claus,\n\nMy name is {name}, I am {age} years old, and I have been {behavior} this year. Here is my letter:\n\n{letter_content}\n\nBest wishes,\n{name}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=500
        )
        
        santa_response = response.choices[0].message['content'].strip()
        st.success("Your letter has been sent to Santa Claus!")
        st.subheader("Santa's Response:")
        st.write(santa_response)
    else:
        st.error("Please provide your name, age, and write something in the letter before sending.")