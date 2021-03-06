import requests
import random


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NWUxYjFkYTc3NzI4ZmZkYTM2OTg2OGUyOTQ3YTBkYSIsInN1YiI6IjYwNzA4MmIwY2QyMDQ2MDA1OGExZjhiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XINtPP3u1t_em2nuU0Hflpjd5lgJpU1L91KYJQIBeaw"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_movies_list(list_type):
    # endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # try:
    #     response.raise_for_status()
    # except:
    #     print("Nie ma takiej listy")
    # finally:
    #     response = requests.get(
    #         "https://api.themoviedb.org/3/movie/popular", headers=headers)
    # return response.json()
    return call_tmdb_api(f"movie/{list_type}")

# def get_popular_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/popular"
#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    random.shuffle(data["results"])
    return data["results"][:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    # endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # return response.json()
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    # endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # return response.json()["cast"]
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

def get_movie_images(movie_id):
    # endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    # return response.json()
    return call_tmdb_api(f"movie/{movie_id}/images")