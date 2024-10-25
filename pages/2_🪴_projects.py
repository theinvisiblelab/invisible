import streamlit as st

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

st.header("🪴 Current Projects")

st.write("&nbsp;")

with st.expander("Pictopercept", expanded = False):
    st.write("""
            _PictoPercept_ is an innovative, open-source software that utilizes visual wiki surveys to assess societal biases and perceptions, particularly focusing on youth perceptions of occupational roles. By integrating visual stimuli into pairwise comparison methodologies, _PictoPercept_ unobtrusively captures perceptions related to potentially sensitive topics like gender and ethnic stereotypes in professions. Participants engage by selecting between images representing diverse demographic attributes, contributing to a dynamic and democratic data collection process. This method leverages the human brain's visual processing capabilities, providing researchers with nuanced insights into the formation and reinforcement of social stereotypes through a Bayesian statistical model. Aimed initially at Dutch youth, _PictoPercept_ is poised to significantly advance bias assessment methodologies and contribute valuable data to the fields of communication science and beyond. Learn more [here](https://pictopercept.streamlit.app/).
        """)

with st.expander("N|uu", expanded = False):
    st.write("The Internet is a very unfair representation of human linguistic diversity. `N|uu` is an attempt to make these stark inequalities visible by quantifying internet representation for all languages scripted by humans. Learn more [here](https://invisiblelang.streamlit.app/).")