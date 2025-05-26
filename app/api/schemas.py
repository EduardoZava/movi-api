from pydantic import BaseModel
from typing import List

class ReviewCreate(BaseModel):
    imdb_id: str
    user_opinion: str
    user_rating: int

class ReviewResponse(BaseModel):
    user_opinion: str
    user_rating: int

class MovieResponse(BaseModel):
    title: str
    year: int
    imdb_id: str
    genre: str
    director: str
    actors: List[str]
    imdb_rating: str
    plot: str
    reviews: List[ReviewResponse]

class MovieSearchRequest(BaseModel):
    title: str | None = None
    year: int | None = None
