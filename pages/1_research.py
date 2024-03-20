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


st.title("🕯️ the (in)visible lab")
st.write("_enabling fairer knowledge access_")
st.write("&nbsp;")

st.header("research")

st.write("&nbsp;")
st.write("&nbsp;")
st.write("&nbsp;")

with st.expander("About the (in)visible lab"):
    st.write("""
        The internet has transformed how we live, affecting our social lives, economies, politics, and culture. But it’s not just fake news or biased articles we should worry about. There’s a hidden issue that’s just as tricky: we’re only seeing part of the picture, or just the tip of the information iceberg. When we search online or scroll across media feeds, the first thing that pops up gets most of the attention — more than half the clicks, actually. Then what about the relevant content that almost never makes it to the top of the list?

    It turns out a lot of information just doesn’t get seen. We tackle this challenge by creating a way to dynamically measure how visible information really is when we are online. The next step? We are starting to put together a website for everyone to use that will spotlight obscure films, music, and books that are almost always missed out. Each day, this platform will leverage data from sources like IMDb, the Milling Songs Database, and the Free Music Archive to find and share such hidden gems. This way, we can all contribute to the development of a fairer internet enabling access to truly diverse knowledge.
    """
    )
