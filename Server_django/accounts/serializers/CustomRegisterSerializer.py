from django.db import models
from django.db.models import fields

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from movies.serializers.GenreSerializer import GenreSerializer


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)
    email = serializers.EmailField(required=False)
    like_genres = GenreSerializer(many=True, required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['like_genres'] = self.validated_data.get('like_genres', [])
        return data_dict