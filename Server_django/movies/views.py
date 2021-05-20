import pprint

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
import requests

# Create your views here.

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
