import streamlit as st
import random

st.title("(in)visible")
# st.write("Enabling fairer knowledge access")
st.write("&nbsp;")
st.write("Choose a category to explore invisible content.")

# Define a list of films as above
films = [
    {
        "title": "The Invisible Man",
        "director": "James Whale",
        "year": 1933,
        "plot": "After developing a way to become invisible, Dr. Jack Griffin, a scientist, becomes tragically insane and vengeful."
    },
    {
        "title": "Hollow Man",
        "director": "Paul Verhoeven",
        "year": 2000,
        "plot": "Scientists discover how to make humans invisible, but their test subject becomes an insane killer who stalks the team."
    },
    {
        "title": "Memoirs of an Invisible Man",
        "director": "John Carpenter",
        "year": 1992,
        "plot": "After a freak accident, a man is rendered invisible and becomes pursued by a ruthless government agent."
    },
    {
        "title": "The Invisible",
        "director": "David S. Goyer",
        "year": 2007,
        "plot": "A teenager is attacked and left for dead, but finds himself trapped in a ghostly limbo where no one can see him."
    },
    {
        "title": "Invisible Agent",
        "director": "Edwin L. Marin",
        "year": 1942,
        "plot": "The grandson of the original Invisible Man uses his grandfather's formula to spy on Nazi Germany during WWII."
    },
    {
        "title": "The Invisible Woman",
        "director": "A. Edward Sutherland",
        "year": 1940,
        "plot": "A department store model volunteers for an experiment with an invisibility machine."
    },
    {
        "title": "Invisibility",
        "director": "Paolo Bertola",
        "year": 2013,
        "plot": "Explores the concept of invisibility from a philosophical perspective, questioning the visibility in society and relationships."
    },
    {
        "title": "The Invisible Boy",
        "director": "Gabriele Salvatores",
        "year": 2014,
        "plot": "A shy and unassuming boy discovers he has the power to become invisible, leading him on an unexpected adventure."
    },
    {
        "title": "The Invisible Man Returns",
        "director": "Joe May",
        "year": 1940,
        "plot": "Accused of a murder he didn't commit, a man uses an invisibility formula to escape prison and clear his name."
    },
    {
        "title": "The Invisible Man's Revenge",
        "director": "Ford Beebe",
        "year": 1944,
        "plot": "A man uses an invisibility formula to exact revenge on those he believes have wronged him."
    },
    {
        "title": "Abbott and Costello Meet the Invisible Man",
        "director": "Charles Lamont",
        "year": 1951,
        "plot": "The comedy duo helps a man wrongly accused of murder, who uses an invisibility serum to evade the police."
    },
    {
        "title": "Invisible Sister",
        "director": "Paul Hoen",
        "year": 2015,
        "plot": "A science project goes awry, making a teenager's sister become invisible, leading to unexpected antics and a closer bond."
    },
    {
        "title": "The Amazing Transparent Man",
        "director": "Edgar G. Ulmer",
        "year": 1960,
        "plot": "An ex-army major uses a prisoner to become invisible and steal nuclear material for an experiment."
    },
    {
        "title": "Invisible Avenger",
        "director": "James Wong Howe, Ben Parker",
        "year": 1958,
        "plot": "A man with the power of invisibility is drawn into a conflict with a gangster to protect a refugee."
    },
    {
        "title": "The League of Extraordinary Gentlemen",
        "director": "Stephen Norrington",
        "year": 2003,
        "plot": "A team of extraordinary figures, including an invisible man, is assembled to stop a terrorist plot."
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "director": "Chris Columbus",
        "year": 2001,
        "plot": "A young wizard finds an invisibility cloak, which plays a crucial role in his adventures at Hogwarts."
    },
    {
        "title": "Predator",
        "director": "John McTiernan",
        "year": 1987,
        "plot": "A commando unit in the Central American jungle faces off against an alien warrior that uses invisibility to hunt."
    },
    {
        "title": "Ghost in the Shell",
        "director": "Rupert Sanders",
        "year": 2017,
        "plot": "In the near future, a cyber-enhanced soldier hunts down a hacker, using therm-optic camouflage to become invisible."
    },
    {
        "title": "The Invisible Maniac",
        "director": "Adam Rifkin",
        "year": 1990,
        "plot": "A mad scientist escapes from a mental institution and becomes a high school physics teacher, with deadly consequences."
    },
    {
        "title": "Invisible Strangler",
        "director": "John Florea",
        "year": 1976,
        "plot": "An invisible man escapes from an asylum and seeks vengeance against those responsible for his wrongful imprisonment."
    }
]

# Dropdown for page navigation
page = st.selectbox("", ('', 'Films', 'Music', 'Books', 'News'))

if page == 'Films':

    if st.button('Find an invisible film!'):
        selected_film = random.choice(films)

        st.write(f"**{selected_film['title']}** ({selected_film['year']})")

        random_number = random.randint(1, 250)
        image_url = f"https://picsum.photos/id/{random_number}/200/300"
        st.markdown(f"<img src='{image_url}'/>", unsafe_allow_html=True)

        st.write("&nbsp;")
        st.write(selected_film['plot'])

        table_markdown = f"""
        | Title          | Director       | Year |
        |----------------|----------------|------|
        | {selected_film['title']} | {selected_film['director']} | {selected_film['year']} |
        """
        st.markdown(table_markdown)

        st.write("&nbsp;")
        st.warning("Dummy responses above! Application under development...")

elif page == 'Music':
    # Here, you can add functionality to find invisible music.
    # Since we're dealing with dummy responses for now:
    st.warning("Application under development...")

elif page == 'Books':
    # Similarly, add functionality for finding invisible books.
    st.warning("Application under development...")

elif page == 'News':
    # And functionality for finding invisible news.
    st.warning("Application under development...")

st.write("&nbsp;")
st.write("&nbsp;")
st.write("&nbsp;")
with st.expander("What is this about?"):
    st.write("""
        The internet has transformed how we live, affecting our social lives, economies, politics, and culture. But it’s not just fake news or biased articles we should worry about. There’s a hidden issue that’s just as tricky: we’re only seeing part of the picture, or just the tip of the information iceberg. When we search online or scroll across media feeds, the first thing that pops up gets most of the attention — more than half the clicks, actually. Then what about the relevant content that almost never makes it to the top of the list?

It turns out a lot of information just doesn’t get seen. We tackle this challenge by creating a way to dynamically measure how visible information really is when we are online. The next step? We are starting to put together a website for everyone to use that will spotlight obscure films, music, and books that are almost always missed out. Each day, this platform will leverage data from sources like IMDb, the Milling Songs Database, and the Free Music Archive to find and share such hidden gems. This way, we can all contribute to the development of a fairer internet enabling access to truly diverse knowledge.
    """
    )