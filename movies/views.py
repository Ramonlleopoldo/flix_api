from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import MovieModel
from movies.serializers import MovieSerializer, MovieListDetailView
from reviews.models import ReviewModels


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MovieModel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailView
        return MovieSerializer


class MovieRestriveUpdatedeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MovieModel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailView
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = MovieModel.objects.all()

    def get(self, request):
        total_movie = self.queryset.count()
        movie_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_review = ReviewModels.objects.count()
        average_rating = ReviewModels.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return response.Response(
            data={"total_movie": total_movie, "movie_by_genre": movie_by_genre, "total_review": total_review, "average_rating": round(average_rating, 1) if average_rating else 0},
            status=status.HTTP_200_OK
        )
