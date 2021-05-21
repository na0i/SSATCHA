from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pprint
import requests

from .models import Movie, Genre
from .api_request import get_genre, recommend_movies, get_movie_info, search, get_providers


# 장르 데이터는 처음부터 db에 가지고 있는 것이 좋을까요..?
# 사실 그렇다면 합쳐도 되는 걸..
# 이거 굳이 뷰에서 가지고 있을 필요가 없슴미당
def get_genre_data():
    datum = get_genre()

    for data in datum:
        genre = Genre(genre_id=data['id'], name=data['name'])
        genre.save()




## 대충 이런 느낌..
@api_view(['GET', 'POST'])
def create_movie(request, movie_key):
    # api 요청 보내서 영화 데이터 만들기
    if request.method == 'POST':
        if not Movie.objects.filter(movie_key=movie_key):
            api_key = '1f6f8f7d643eea003df9f19e38d13c3d'
            url = f'https://api.themoviedb.org/3/movie/{movie_key}?api_key={api_key}&language=en-US'
            response = requests.get(url).json()
            pprint.pprint(response)

            movie = {
                'movie_key': movie_key,
                'title': response['title'],
                'overview': response['overview'],
                'release_date': response['release_date'],
                'poster_path': response['poster_path'],
            }

            serializer = MovieSerializer(data=movie)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        movie = get_object_or_404(Movie, movie_key=movie_key)
        serializer = MovieSerializer(instance=movie)
        return Response(data=serializer.data)
