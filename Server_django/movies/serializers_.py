from rest_framework import serializers
from .models import Genre, Movie
try:
    from accounts.serializers import UserSerializer
except ImportError:
    import sys
    UserSerializer = sys.modules[__package__ + '.UserSerializer']

try:
    from board.serializers import ReviewListSerializer
except ImportError:
    import sys
    ReviewListSerializer = sys.modules[__package__ + '.ReviewListSerializer']



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    overview = serializers.CharField(min_length=1, required=False, allow_blank=True)
    release_date = serializers.DateField(required=False)
    poster_path = serializers.CharField(max_length=200, required=False)
    original_language = serializers.CharField(max_length=50, required=False, allow_blank=True)
    genres = GenreSerializer(many=True, required=False)
    like_users = UserSerializer(many=True, read_only=True)
    # 리뷰의 경우 null 가능하도록 해야 하나요?
    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'review_set')
        fields = '__all__'


# 단일 영화
class MovieLikeUserSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('like_users', )


# 전체 영화 목록
# 만약 영화 리스트 화면에서 보이고 싶은 데이터가 추가적으로 존재하는 경우,
# 여기서 필드에 추가해주면 되겠습니다.
# 어찌되었든 추가작업이 필요할 거 같네용
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'id', 'original_title', )


# class InitialMovieDataSerializer(serializers.ModelSerializer):
#
#
# # 최초에 추천하는 영화랑 이런거 보내주는 시리얼라이져..
