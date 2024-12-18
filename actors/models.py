from django.db import models


NATIONALITY_CHOICES = (
    ("USA", "Estados Unidos"),
    ("Brazil", "Brasil"),
)


class ActorsModel(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
