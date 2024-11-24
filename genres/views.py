from rest_framework import generics
from genres.models import GenresModel
from genres.serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer
