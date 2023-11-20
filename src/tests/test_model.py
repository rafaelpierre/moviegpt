from moviegpt.data.movie import Movie, Movies
from tests.fixtures import movie
from pydantic import ValidationError
import pytest

def test_instantiate_movie():

    with pytest.raises(ValidationError):
        movie = Movie()

def test_instantiate_movies(movie):

    movie = Movie.parse_raw(movie)
    movies = Movies(movies = [movie])

    pass
