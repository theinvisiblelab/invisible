import streamlit as st

st.set_page_config(page_icon="🕯️", page_title="The (In)visible Hub", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("🕯️ The (In)visible Hub")
st.write(":gray[_Enabling fairer knowledge access_]")
st.write("&nbsp;")

st.sidebar.info("**Supported By** \n\n 🌱 Amsterdam School of Communication Research \n\n 🌱 Social and Behavioural Data Science Centre, University of Amsterdam \n\n Reach out to our [team](/team) for feedback and/or collaboration.")

st.header("🪴 Projects")


