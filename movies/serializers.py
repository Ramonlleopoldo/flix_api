from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorsSerializers
from movies.models import MovieModel
from genres.models import GenresModel
from genres.serializers import GenreSerializer
from actors.models import ActorsModel

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=GenresModel.objects.all(),
    )
    release_data = serializers.DateField(required=False, allow_null=True)
    actors = serializers.PrimaryKeyRelatedField(
        queryset=ActorsModel.objects.all(),
        many=True,
    )
    resume = serializers.CharField(required=False, allow_null=True, allow_blank=True)

class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieModel
        fields = '__all__'
        extra_kwargs = {
            'resume': {'required': False, 'allow_null': True, 'allow_blank': True},
            'release_data': {'required': False, 'allow_null': True},
        }

    def validate_release_data(self, value):
        if value and value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900.')
        return value

    def validate_resume(self, value):
        if value and len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior do que 500 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorsSerializers(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MovieModel
        fields = ['id', 'title', 'genre', 'actors', 'release_data', 'rate', 'resume']

    def get_rate(self, obj):
        rating = obj.movie_reviews.aggregate(Avg('rating'))['rating__avg']
        if rating:
            return round(rating, 1)
        return None

class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_rating = serializers.FloatField()
