import pytest
import shutil

@pytest.fixture()
def review():

    data = """
        Alexandra Thompson, a 19-year-old computer science sophomore with a 3.7 GPA,
        is a member of the programming and chess clubs who enjoys pizza, swimming, and hiking
        in her free time in hopes of working at a tech company after graduating from the University of Washington.
    """

    return data

@pytest.fixture(scope = "session")
def chroma_helper():
    
    from moviegpt.data.chroma import ChromaHelper
    return ChromaHelper(path = ".tox/db")

@pytest.fixture(scope = "session")
def chroma_collection(chroma_helper):
    shutil.rmtree(".tox/db")
    return chroma_helper.client.create_collection(name = "movies")

@pytest.fixture(scope = "session")
def movie():

    movie_str = """
    {
        "title": "The Grudge",
        "year": 2020,
        "cast": [
        "Andrea Riseborough",
        "Demián Bichir",
        "John Cho",
        "Betty Gilpin",
        "Lin Shaye",
        "Jacki Weaver"
        ],
        "genres": [
        "Horror",
        "Supernatural"
        ],
        "href": "The_Grudge_(2020_film)",
        "extract": "The Grudge is a 2020 American psychological supernatural horror film written and directed by Nicolas Pesce. Originally announced as a reboot of the 2004 American remake and the original 2002 Japanese horror film Ju-On: The Grudge, the film ended up taking place before and during the events of the 2004 film and its two direct sequels, and is the fourth installment in the American The Grudge film series. The film stars Andrea Riseborough, Demián Bichir, John Cho, Betty Gilpin, Lin Shaye, and Jacki Weaver, and follows a police officer who investigates several murders that are seemingly connected to a single house.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/en/3/34/The_Grudge_2020_Poster.jpeg",
        "thumbnail_width": 220,
        "thumbnail_height": 326
    }
    """

    return movie_str

