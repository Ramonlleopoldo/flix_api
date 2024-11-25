from rest_framework import generics
from actors.models import ActorsModel
from actors.serializer import ActorsSerializers

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = ActorsModel.objects.all()
    serializer_class = ActorsSerializers

class ActorsReciveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActorsModel.objects.all()
    serializer_class = ActorsSerializers
