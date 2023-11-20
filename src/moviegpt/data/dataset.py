"""Helper script to download Wikipedia movie data."""

from pydantic import BaseModel
import httpx
import pandas as pd
import logging

class MovieDataset(BaseModel):

    base_url: str = "https://github.com/prust/wikipedia-movie-data/raw/master/movies-{}s.json"
    