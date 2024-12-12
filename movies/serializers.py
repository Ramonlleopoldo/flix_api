from rest_framework import serializers
from movies.models import MovieModel
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = MovieModel
        fields = '__all__'

    def get_rate(self,obj):
        rate = obj.movie_review.aggregate(Avg('rating'))['rating__avg']
        if rate:
            return round(rate,1)
        return None
            

    def validate_release_data(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento deve ser maior que 1990.')
        else :
            return value
    def validate_resume(self,value):
        if len(value)>600:
            raise serializers.ValidationError("O resumo do filme nao pode ter mais de 200 caracteres")
        else:
            return value
        
