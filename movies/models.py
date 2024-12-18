from django.db import models
from genres.models import GenresModel
from actors.models import ActorsModel


class MovieModel(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(GenresModel, on_delete=models.PROTECT, related_name='movie_genre')
    actors = models.ManyToManyField(ActorsModel, related_name='movie_actors')
    resume = models.TextField(blank=True, null=True)
    release_data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
