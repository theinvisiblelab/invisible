import streamlit as st
import random

# Set page to wide mode
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

st.sidebar.info("The (in)visible lab is housed in the Amsterdam School of Communication Research, University of Amsterdam. Please reach out to our [team](https://theinvisiblelab.streamlit.app/team) for more information.")


option = st.radio("Calculate invisible information by:",
                    ('Searching the internet', 'Uploading your own dataset'))

st.write("&nbsp;")
if option == 'Searching the internet':
    # User opts to search the internet
    search_query = st.text_input("Enter a search query").lower().strip()
    if search_query:
        st.info("Search functionality to be implemented...")

elif option == 'Uploading your own dataset':
    # User opts to upload their own dataset
    st.write("You can upload CSV or excel files.")
    uploaded_file = st.file_uploader("Choose your file")
    if uploaded_file is not None:
        # Assuming a CSV file, you can adjust based on your needs
        # To handle the uploaded file, you might use Pandas, for example:
        # df = pd.read_csv(uploaded_file)
        # st.write(df)
        st.info("File upload functionality to be implemented...")
        # Implement your file handling and analysis functionality here



st.write("&nbsp;")
st.write("&nbsp;")
st.write("&nbsp;")

with st.expander("About the (in)visible lab"):
    st.write("""
       The technological revolution of the Internet has digitised the social, economic, political, and cultural activities of billions of humans. While researchers have paid due attention to concerns of misinformation and bias, these obscure a much less researched though equally challenging problem - that of rising 'information invisibility'. On one hand, the problem of invisible information stems from the very nature of explicitly 'ranked' information on any media platforms (search results, social media feeds, news headlines, to name a few), a ranking determined for us (and not by us) through media platforms built to maximise engagement. On the other hand, as humans constantly facing information overloads, our limited mental capacities leave us with little choice but to consume the tip of these pre-ranked information icebergs. Operating at an unprecedented scale across space-time, such behaviour renders a majority of digital human knowledge as invisible. Facing this conundrum, a fundamental and urgent question we must ask is: _how much information remains 'invisible' from us as we navigate our digitised lives?_ In light of this, the aim of The Invisible Lab is to provide a platform to dynamically quantify invisible information, as well as to actively make invisible information/media sources visible.
    """
    )