from src.tests.fixtures import (
    review,
    chroma_collection,
    chroma_helper
)


def test_add_document(review, chroma_collection):

    chroma_collection.add(
        documents = [review],
        metadatas = [{"name": "Test Movie"}],
        ids = ["movie_1"]
    )

    pass

def test_query_document(review, chroma_collection):

    results = chroma_collection.query(
        query_texts = [review],
        n_results = 1
    )

    assert results
    




