from rest_framework import generics
from reviews.models import ReviewModels
from reviews.serializers import ReviewSerializers

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializers

class ReviewRestriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializers
    
