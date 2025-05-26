from typing import List
from dataclasses import dataclass, field

@dataclass
class Review:
    user_opinion: str
    user_rating: int

    def __post_init__(self):
        if not (1 <= self.user_rating <= 10):
            raise ValueError("user_rating must be between 1 and 10")

@dataclass
class Movie:
    imdb_id: str
    title: str
    year: int
    genre: str
    director: str
    actors: List[str]
    imdb_rating: str
    plot: str
    reviews: List[Review] = field(default_factory=list)

    def add_review(self, review: Review):
        self.reviews.append(review)
