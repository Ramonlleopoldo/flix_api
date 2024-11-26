
from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView,GenreRetriveUpdateDelete
from actors.views import ActorListCreateView,ActorsReciveUpdateDeleteView
from movies.views import MovieListCreateView, MovieRestriveUpdatedeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreListCreateView.as_view(), name= 'genres_list_create'),
    path('genres/<int:pk>/',GenreRetriveUpdateDelete.as_view(), name='genre_detail_update_delete'),
   
    path('actors/',ActorListCreateView.as_view(), name="actors_list_create" ),
    path('actors/<int:pk>/',ActorsReciveUpdateDeleteView.as_view(), name="actors_details_update_delete" ),
   
    path('movies/',MovieListCreateView.as_view(), name='movie_list_create'),
    path('movies/<int:pk>/',MovieRestriveUpdatedeleteView.as_view(), name='movie_details_update_delete'),
]
