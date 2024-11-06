import streamlit as st
import uuid
import time
from streamlit_lottie import st_lottie

def stream_data():
    for word in TEXT.split(" "):
        yield word + " "
        time.sleep(0.02)

col1, col2 = st.columns([2, 1])

with col2:
    st.image("images/iceberg.gif")

with col1:
    TEXT = """
    The Internet has transformed our lives, but has also introduced the challenge of _invisible information_ — vital knowledge we consistently miss out on. In today's world of exponentially growing information, algorithms prioritize content that maximizes consumption, and humans deal with this already priotized content by consistently consuming the tip of the information iceberg. This is the challenge that The (In)visible Lab aims to tackle — by understanding, quantifying, and boosting invisible knowledge across the Internet.

    We are presently leading research along four themes:
    """

    # Initialize user ID and display text
    if "userid" not in st.session_state:
        st.session_state.userid = str(uuid.uuid4())
        st.write(stream_data)
    else:
        st.write(TEXT)


tab1, tab2, tab3, tab4 = st.tabs(["(In)visible", "PictoPercept", "Lost Without Translation", "Beyond Words"])

with tab1:
    col_a, col_b = st.columns([3, 1])
    with col_a:
        discover_choice = st.radio("Choose a category to discover invisible content.", ["Films", "Music", "Books", "News"])
        if discover_choice == "Films":
            if st.button('Find an invisible film!', type='primary'):
                st.info("Application under development...")

        if discover_choice == "Music":
            if st.button('Find an invisible piece of music!', type='primary'):
                st.info("Application under development ...")

        if discover_choice == "Books":
            if st.button('Find an invisible book!', type='primary'):
                st.info("Application under development...")

        if discover_choice == "News":
            if st.button('Find some invisible news!', type='primary'):
                st.info("Application under development...")
    with col_b:
        st_lottie("https://lottie.host/ec3d9846-8444-4cfc-ae03-502e05cb7b93/MMktMDfAsz.json")
with tab2:
    col_c, col_d = st.columns([2.6, 1])
    with col_c:
        st.write("PictoPercept is an innovative visual survey approach designed to reveal invisible biases and preferences that traditional surveys fail to capture. Using rapid, visual forced-choice tasks, it captures subconscious attitudes shaped by digital media exposure and social identity cues, which respondents might otherwise conceal in favor of social desirability.")
        btn2 = st.link_button("Go to PictoPercept", url = "https://pictopercept.streamlit.app/", use_container_width=True, type="primary")
    with col_d:
        st_lottie("https://lottie.host/a0357f2b-b951-4f69-b9e8-35b36e79b386/9B0IQaQ77q.json")
with tab3:
    col_e, col_f = st.columns([3, 1])
    with col_e:
        st.write("The Internet is a very unfair representation of human linguistic diversity. Lost Without Translation is an attempt to make these stark inequalities visible by quantifying and boosting online visibility for all living languages scripted by humans.")
        btn3 = st.link_button("Go to Lost Without Translation", url = "https://invisiblelang.streamlit.app/", use_container_width=True, type="primary")
    with col_f:
        st_lottie("https://lottie.host/3bfd556b-b768-4374-9c7f-06cc18463d6a/tkfyhGMudo.json")
with tab4:
    col_g, col_h = st.columns([3, 1])
    with col_g:
        st.write("Almost all of knowledge visible to us is built on communication among humans. Could we make the invisible visible by developing ways to communicate information effectively beyond our species? Beyond Words is attempt to answer these challenging questions.")
        btn4 = st.button("Go to Beyond Words", use_container_width=True, type="primary")
        if btn4:
            st.info("🪜 Project web page under development!")
    with col_h:
        st_lottie("https://lottie.host/480758a4-5f42-4cec-8d52-04feb1c76366/Plw1GhxvDZ.json")