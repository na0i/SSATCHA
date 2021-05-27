from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Genre

User = get_user_model()


def save_genres(user, genres):
    user = get_object_or_404(User, pk=user.pk)
    for genre in genres:
        user.like_genres.add(genre)
        user.save()


# 회원가입 정보 저장
class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.save()
        save_genres(user, data.get('like_genres', []))
        return user

'''
{
    "username": "lki1243",
    "email": "dlk12@nael.com",
    "password1": "trew5498",
    "password2": "trew5498",
    "nickname": "tldk",
    "like_genres": [{"id": 18, "name": "드라마"}, {"id": 36, "name": "역사"}]
}
->
"like_genres": [
        {
            "id": [
                "genre with this id already exists."
            ]

'''