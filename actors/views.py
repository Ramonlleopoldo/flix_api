from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import ActorsModel
from actors.serializers import ActorsSerializers

class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ActorsModel.objects.all()
    serializer_class = ActorsSerializers

class ActorsReciveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ActorsModel.objects.all()
    serializer_class = ActorsSerializers
