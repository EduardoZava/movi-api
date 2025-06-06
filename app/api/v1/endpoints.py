from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.application.services import MovieService
from app.api.v1.schemas import ReviewCreate, MovieResponse
from app.adapters.http.omdb_client import OMDbMovieProvider
from app.adapters.repository.postgres_repository import PostgresMovieRepository
from infrastructure.db.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

def get_movie_service(db: Session = Depends(get_db)) -> MovieService:
    repo = PostgresMovieRepository(db)
    # OMDb API key should come from environment/config in real app
    provider = OMDbMovieProvider(api_key="38e11782")
    service = MovieService(repo, provider)
    return service

@router.post("/create-movie", status_code=201)
def create_review(review: ReviewCreate, service: MovieService = Depends(get_movie_service)):
    service.add_review(review.imdb_id, review.user_opinion, review.user_rating)
    return {"message": "Review added"}

@router.get("/search-movie", response_model=List[MovieResponse])
def search_movies(imdb_id: Optional[str] = Query(None),
                  title: Optional[str] = Query(None),
                  year: Optional[int] = Query(None),
                  service: MovieService = Depends(get_movie_service)):
    if imdb_id:
        movie = service.get_consolidated_movie(imdb_id)
    else:
       if title and year:
          movie = service.get_consolidated_movie(title=title, year=year)
       else:
          raise HTTPException(status_code=400, detail="imdb_id or title and year query parameter required")
    
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    # Convert movie to response model
    #movie_response = MovieResponse.from_domain(movie)
    # Return a list with a single movie response
    return [movie]
