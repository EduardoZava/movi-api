from typing import List
from app.application.ports import MovieRepositoryPort, MovieProviderPort
from app.domain.entities import Movie, Review

class MovieService:
    def __init__(self, repo: MovieRepositoryPort, provider: MovieProviderPort):
        self.repo = repo
        self.provider = provider

    def add_review(self, imdb_id: str, user_opinion: str, user_rating: int):
        review = Review(user_opinion=user_opinion, user_rating=user_rating)
        self.repo.save_review(imdb_id, review)

    def get_consolidated_movie_by_imdb(self, imdb_id: str) -> Movie | None:
        movie = self.provider.get_movie_details_by_imdb(imdb_id)
        if not movie:
            return None
        reviews = self.repo.get_reviews_by_imdb_id(imdb_id)
        movie.reviews = reviews
        return movie
    
    def get_consolidated_movie(self, title: str, year: int) -> Movie | None:
        movie = self.provider.get_movie_details(title=title, year=year)
        if not movie:
            return None
        reviews = self.repo.get_reviews_by_imdb_id(movie.imdb_id)
        movie.reviews = reviews
        return movie
