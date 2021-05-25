from django.shortcuts import get_object_or_404, HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from movies.models import Movie

from django.contrib.auth import get_user_model
User = get_user_model()


# 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 읽기+댓글목록, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def read_or_update_or_delete_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    # 리뷰 수정
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if review.user == request.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie)
                return Response(serializer.data, status=status.HTTP_200_OK)

    # 리뷰 삭제
    elif request.method == 'DELETE':
        # 작성자가 삭제..
        if review.user == request.user:
            review.delete()
            data = {
                'success': True,
                'message': f'<{review.title}> 삭제 성공'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    # GET 의 경우
    # 수정 삭제 눌렀지만, 권한이 없는 유저의 경우 흘러서 여기로 내려올 것 같습니다.
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정, 삭제, 대댓글
@api_view(['PUT', 'DELETE', 'POST'])
def update_or_delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 댓글 수정
    if request.method == 'PUT':
        if comment.user == request.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                if comment.reply_to:
                    serializer.save(review=review, user=request.user, reply_to=comment.reply_to)
                else:
                    serializer.save(review=review, user=request.user)  # 수정할 때, 부모댓글 연결 어떻게 하죠..?
                return Response(serializer.data, status=status.HTTP_200_OK)

    # 댓글 삭제
    if request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            data = {
                'success': True,
                'message': '댓글이 성공적으로 삭제되었습니다.'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    # 대댓글 생성
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user, reply_to=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 권한 없는 사용자가 버튼을 클릭한 경우 리뷰페이지로 이동
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


# 리뷰 좋아요
@api_view(['POST'])
def like_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            data = {
                'like': False,
                'count': review.like_users.count()
            }
        else:
            review.like_users.add(user)
            data = {
                'like': True,
                'count': review.like_users.count()
            }

        return Response(data=data, status=status.HTTP_202_ACCEPTED)

    # 회원이 아닌 경우
    # return HttpResponseRedirect('rest-auth/login/')
    return HttpResponseRedirect('http://127.0.0.1:8000/rest-auth/login/')





