from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import GenresModel
from genres.serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer
