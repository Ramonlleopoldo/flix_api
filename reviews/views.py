from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import ReviewModels
from reviews.serializers import ReviewSerializers


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializers


class ReviewRestriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializers
