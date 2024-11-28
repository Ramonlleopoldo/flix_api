from django.db import models
from movies.models import MovieModel
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewModels(models.Model):
    user_name = models.CharField(max_length=200)
    movie = models.ForeignKey(MovieModel, on_delete=models.PROTECT , related_name='movie_review')
    rating = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    coments = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Usuario:{self.user_name} - Filme:{self.movie}'
