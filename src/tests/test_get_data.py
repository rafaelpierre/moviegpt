from unittest import mock
from moviegpt.data.movie import get_data


@mock.patch("httpx.get", mock.MagicMock())
def test_get_data():

    import httpx
    get_data()
    httpx.get.assert_called()

