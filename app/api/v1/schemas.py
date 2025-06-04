from pydantic import BaseModel as ScBaseModel
from typing import List

class ReviewCreate(ScBaseModel):
    imdb_id: str
    user_opinion: str
    user_rating: int

class ReviewResponse(ScBaseModel):
    user_opinion: str
    user_rating: int

class MovieResponse(ScBaseModel):
    title: str
    year: int
    imdb_id: str
    genre: str
    director: str
    actors: List[str]
    imdb_rating: str
    plot: str
    reviews: List[ReviewResponse]

class MovieSearchRequest(ScBaseModel):
    title: str | None = None
    year: int | None = None
