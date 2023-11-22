from moviegpt.providers.rag import RAGProvider
from moviegpt.prompts.recommendation import RecommendationPrompt
from tests.fixtures import api_key
from unittest import mock
import logging


def test_provider(api_key):
    provider = RAGProvider(api_key = api_key)
    provider.create_index()

    pass

@mock.patch("httpx.post", mock.MagicMock())
def test_query(api_key):

    from httpx import post

    provider = RAGProvider(api_key = api_key)
    prompt = RecommendationPrompt(details = "super hero movies")
    response = provider.query(prompt = prompt)
    logging.info(response)

    assert False