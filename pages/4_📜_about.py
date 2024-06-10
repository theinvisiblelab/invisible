import streamlit as st
import time

st.set_page_config(page_icon="🕯️", page_title="The (In)visible Lab", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("🕯️ The (In)visible Lab")
st.write(":gray[_Enabling fairer knowledge access_]")
st.write("&nbsp;")

st.sidebar.info("**Supported By** \n\n 🌱 Amsterdam School of Communication Research \n\n 🌱 Social and Behavioural Data Science Centre, University of Amsterdam \n\n Reach out to our [team](/team) for feedback and/or collaboration.")

st.header("📜 About Us")

TEXT = """
       The technological revolution of the Internet has digitised the social, economic, political, and cultural activities of billions of humans. While researchers have paid due attention to concerns of misinformation and bias, these obscure a much less researched though equally challenging problem - that of rising 'information invisibility'. On one hand, the problem of invisible information stems from the very nature of explicitly 'ranked' information on any media platforms (search results, social media feeds, news headlines, to name a few), a ranking determined for us (and not by us) through media platforms built to maximise engagement. On the other hand, as humans constantly facing information overloads, our limited mental capacities leave us with little choice but to consume the tip of these pre-ranked information icebergs. Operating at an unprecedented scale across space-time, such behaviour renders a majority of digital human knowledge as invisible. 
         
      Facing this conundrum, a fundamental and urgent question we must ask is: _how much information remains 'invisible' from us as we navigate our digitised lives?_ In light of this, the aim of The (In)visible Lab is to provide a platform to dynamically quantify invisible information, as well as to actively make invisible information/media sources visible.
    """

def stream_data():
    for word in TEXT.split(" "):
        yield word + " "
        time.sleep(0.02)

st.write_stream(stream_data)