import requests
from app.adapters.http.translator import convert_omdb_to_movie
from app.domain.entities import Movie

class OMDbMovieProvider:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def get_movie_by_imdb_id(self, imdb_id: str) -> Movie | None:
        params = {"apikey": self.api_key, "i": imdb_id, "plot": "short"}
        try:
            resp = requests.get(self.base_url, params=params, timeout=100)
            if resp.status_code != 200:
                return None
            data = resp.json()
            if data.get("Response") == "False":
                return None
            return convert_omdb_to_movie(data)
        except requests.RequestException:
            return None
    
    def get_movie_details(self, imdb_id: str) -> Movie | None:
        params = {"apikey": self.api_key, "i": imdb_id, "plot": "full"}
        try:
            resp = requests.get(self.base_url, params=params, timeout=100)
            if resp.status_code != 200:
                return None
            data = resp.json()
            if data.get("Response") == "False":
                return None
            return convert_omdb_to_movie(data)
        except requests.RequestException:
            return None
        #return self.get_movie_by_imdb_id(imdb_id)

