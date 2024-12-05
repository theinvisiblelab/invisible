import streamlit as st

st.set_page_config(page_icon="🕯️", page_title="theinvisiblelab.org", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🕯️ [In]visible")
# st.write(":gray[_Enabling fairer knowledge access_]")
st.write("&nbsp;")

home_page = st.Page("invisible.py", title="Home")
team_page = st.Page("team.py", title="Team", icon="🐙")
about_page = st.Page("about.py", title="About", icon="📜")

pg = st.navigation([home_page, team_page, about_page])

st.sidebar.info("**Supported By** \n\n 🌱 Amsterdam School of Communication Research \n\n 🌱 Social and Behavioural Data Science Centre, University of Amsterdam \n\n 🌱 Digital Communication Methods Lab \n\n Reach out to our [team](/team) for feedback and/or collaboration.")

pg.run()