import streamlit as st

st.set_page_config(page_title="Holiday Helper", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Menu Generator", "Postcard Generator", "Carol Generator"])

if page == "Menu Generator":
    from pages import menu_generator
    menu_generator.show()
elif page == "Postcard Generator":
    from pages import postcard_generator
    postcard_generator.show()
else:
    from pages import carol_generator
    carol_generator.show()