from rest_framework import generics
from movies.models import MovieModel
from movies.serializers import MovieSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer

class MovieRestriveUpdatedeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
