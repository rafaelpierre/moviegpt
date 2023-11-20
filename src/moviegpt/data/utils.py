import httpx
import logging
import pandas as pd
import json
from moviegpt.data.movie import Movie, Movies

BASE_URL = "https://github.com/prust/wikipedia-movie-data/raw/master/movies-{}s.json"

def parse_movie_json(movie_json: dict) -> Movie:

    movie = Movie.parse_raw(movie_json)
    return movie

def get_movies(
    base_url: str = BASE_URL,
    start: int = 1960,
    end: int = 2020
) -> Movies:
    """Fetches WikiData for movies.
    
    Parameters:

    start: Starting year
    end: Ending year
    output_path: Path to where dataset will be saved as JSON.
    """

    logging.info(f"Downloading movie info from {start} to {end}")
    decades = [start + (i * 10) for i in range(int((end-start)/10)+1)]
    results = []

    # Makes one GET request for each decade
    for decade in decades:
        response = httpx.get(base_url.format(decade))
        json_movies = response.json()
        movies = Movies([
            Movie.parse_raw(json.dumps(json_movie))
            for json_movie
            in json_movies
        ])
        results.extend(movies)

    return movies