from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import GenresModel
from genres.serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = GenresModel.objects.all()
    serializer_class = GenreSerializer
