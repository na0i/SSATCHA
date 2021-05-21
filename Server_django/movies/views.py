from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pprint
import requests

from .models import Movie, Genre
from .api_request import get_genre, recommend_movies, get_movie_info, search, get_providers, get_genre_list
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer


# 영화 장르 정보 가져오기
@api_view(['POST'])
def get_genre_data(request):
    datum = get_genre()

    results = {
        'saved': 0,
        'failed': 0,
    }

    for data in datum:
        if not Genre.objects.all().filter(pk=data['id']).exists():
            serializer = GenreSerializer(data=data)
            # if serializer.is_valid(raise_exception=True):
            if serializer.is_valid():
                serializer.save()
                results['saved'] += 1
            else:
                results['failed'] += 1

    return Response(data=results)


# 영화 생성 혹은 영화 전체 리스트
@api_view(['GET', 'POST'])
def movie_list_or_create(request):

    # 단일 영화 생성
    if request.method == 'POST':
        # print(request.data['condition'])
        '''
        # recommend_movies(condition, page=1)
        인기 영화 = popular
        top_rated = top_rated

        // 페이지 한개 밖에 없는 듯 //
        개봉예정 = upcoming
        상영중 = now_playing
        '''
        # condition 이 들어서 요청이 왔다면,
        if request.data.get('condition'):
            datum = recommend_movies(request.data['condition'])
            pprint.pprint(datum)
        else:
            datum = request.data

        results = {
            'success': [],
            'failed': []
        }

        for data in datum:
            print(data)
            movie_pk = data['id']
            if not Movie.objects.all().filter(pk=movie_pk):
                serializer = MovieSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    movie = get_object_or_404(Movie, pk=movie_pk)
                    genres = data['genre_ids']
                    # genres = get_genre_list(data['genre_ids'])
                    for genre in genres:
                        movie.genres.add(genre)
                        movie.save()
                    results['success'].append(data['title'])
                # return Response(serializer.data, status=status.HTTP_201_CREATED)

            # movie_pk = request.data['id']
            # if not Movie.objects.all().filter(pk=movie_pk):
            #     serializer = MovieSerializer(data=request.data)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save()
            #         movie = get_object_or_404(Movie, pk=movie_pk)
            #         genres = get_genre_list(request.data['genre_ids'])
            #         for genre in genres:
            #             movie.genres.add(genre)
            #             movie.save()
            #         return Response(serializer.data, status=status.HTTP_201_CREATED)

            # 이미 있는 영화
            else:
                results['failed'].append(data['title'])

        return Response(data=results)

    # 전체 영화 리스트
    elif request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 단일 영화 상세 페이지
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
