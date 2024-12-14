from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import MovieModel
from movies.serializers import MovieSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer

class MovieRestriveUpdatedeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
