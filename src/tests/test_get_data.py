from unittest import mock
from src.moviegpt.data.utils import get_movies


@mock.patch("httpx.get", mock.MagicMock())
def test_get_data():

    import httpx
    get_movies(start = 2010, end = 2020)
    httpx.get.assert_called()

