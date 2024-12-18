from rest_framework import serializers
from genres.models import GenresModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenresModel
        fields = '__all__'
