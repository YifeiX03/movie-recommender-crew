from crewai.tools import BaseTool
from typing import Type, List
from pydantic import BaseModel, Field
import requests


existingGenres = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "Thriller": 53,
    "War": 10752,
    "Western": 37,
}


class MovieApiInput(BaseModel):
    """Input schema for MovieApiTool."""
    genres: List[str] = Field(..., description="Genres of the movie")


class MovieApiTool(BaseTool):
    name: str = "Movie Database API Tool"
    description: str = (
        "Used to make an api call to a movie database to search for movies that relate to the given genre(s)."
        "Choose from existing genres: Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family, Fantasy, History,"
        "Horror, Music, Mystery, Romance, Science Fiction, Thriller, War, Western"
    )
    args_schema: Type[BaseModel] = MovieApiInput

    def _run(self, genres: List[str]) -> str:
        # Implementation goes here
        # Genres
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        url += "&with_genres="
        for genre in genres:
            if not genre in existingGenres:
                continue
            else:
                url += str(existingGenres[genre]) + ","

        print("OUTGOING URL: \n" + url)

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZTIzMGUxODMyMTk2N2Q0YTk1ZGQyOWRjNTE2ZWQ2ZCIsIm5iZiI6MTY3NzAzNzU4MS45ODgsInN1YiI6IjYzZjU5MDBkOWJjZDBmMDBjYzVmMzlkYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.d5rMkCqBZpcHfixJEmiMOGPsX1BTPL-U7x7lyjxwdeo"
        }

        response = requests.get(url, headers=headers)
        print("RESPONSE: \n" + response.text)
        return str(response.text)
