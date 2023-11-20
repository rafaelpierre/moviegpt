from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    title: str
    year: int
    cast: List[str]
    genres: List[str]
    href: str
    extract: str
    thumbnail: str
    thumbnail_width: int
    thumbnail_height: int

class Movies(BaseModel):
    movies: List[Movie]