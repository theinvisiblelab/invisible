import streamlit as st

st.set_page_config(page_icon="🕯️", page_title="the (in)visible lab")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("🕯️ The (In)visible Lab")
st.write("_Enabling fairer knowledge access_")
st.write("&nbsp;")

st.sidebar.info("The (In)visible Lab is housed in the Amsterdam School of Communication Research, University of Amsterdam. Please reach out to our [team](https://theinvisiblelab.streamlit.app/team) for more information.")

st.header("📚 Research")

st.write("Our list of research papers goes here.")
