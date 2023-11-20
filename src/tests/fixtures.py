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

