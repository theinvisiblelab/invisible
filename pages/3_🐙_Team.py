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

st.header("🐙 Team")

st.write("&nbsp;")

with st.expander("Saurabh Khanna", expanded = True):
    st.image("images/saurabh_khanna.jpg", caption="saurabh.khanna@uva.nl", width=200)
    st.write("""
            Saurabh is an Assistant Professor in Communication Science at the University of Amsterdam, and a Research Associate at the University of Oxford. He studies the diversity and limits of human knowledge in an increasingly digitized world. Saurabh received my PhD in education policy and computer science from Stanford University, where he was a Human-centered AI Fellow, a Stanford Data Science Scholar, and a William R and Sara Hart Kimball Fellow. His prior background spans computer science engineering (BITS Pilani), economics (Stanford), and education (TISS).
             More [here](https://saurabh-khanna.github.io/).
        """)

with st.expander("Olga Eisele", expanded = True):
    st.image("images/olga_eisele.jpeg", caption="o.eisele@uva.nl", width=200)
    st.write("""
            Olga is an Assistant Professor in the Corporate Communication Program Group at the Amsterdam School of Communication Research (ASCoR). Before joining ASCoR in 2022, she held positions at the Institute for Advanced Studies in Vienna, Austria, as well as the University of Siegen, Germany. After completing her PhD at Vienna University in 2017, she was Principal Investigator of two research projects on political-media dynamics in times of crisis with a special focus on the European Union. Her research has been published in the European Journal of Political Research , European Union Politics, Journal of Common Market Studies, Political Communication, and Communication Methods & Measures.
        """)

with st.expander("Britta Brugman", expanded = True):
    st.image("images/britta_brugman.jpg", caption="b.c.brugman@uva.nl", width=200)
    st.write("""
            Britta is an Assistant Professor in Communication Science at the University of Amsterdam. Her research focuses on the characteristics of moralising communication and its effects on public opinion formation across various communication contexts: satire, journalism, and communication by and about organisations.
        """)

with st.expander("Sandra Jacobs", expanded = True):
    st.image("images/sandra_jacobs.jpg", caption="s.h.j.jacobs@uva.nl", width=200)
    st.write("""
            Sandra (PhD, Utrecht University, School of Governance) is Assistant Professor in Corporate Communication at the University of Amsterdam, Amsterdam School of Communication Research (ASCoR), the Netherlands. In her research, she focuses on strategic communication of organizations, mediatization, and the mediated construction of societal debates.
        """)

with st.expander("Marina Tulin", expanded = True):
    st.image("images/marina_tulin.jpg", caption="m.tulin@uva.nl", width=200)
    st.write("""
            Marina is an Assistant Professor in Political Communication & Journalism as well as in the sector theme Education, Citizenship and Democracy in a Digital World. She conducts research on mis- and disinformation, fact-checking, media literacy and public trust in institutions like journalism and science.
        """)



    