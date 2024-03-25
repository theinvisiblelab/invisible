import streamlit as st
import random

# Set page to wide mode
st.set_page_config(page_icon="🕯️", page_title="The (In)visible Lab")

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
