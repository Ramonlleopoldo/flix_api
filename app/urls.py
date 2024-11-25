
from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView,GenreRetriveUpdateDelete
from actors.views import ActorListCreateView,ActorsReciveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateView.as_view(), name= 'genres_list_create'),
    path('genres/<int:pk>/',GenreRetriveUpdateDelete.as_view(), name='genre_detail_update_delete'),
    path('actors/',ActorListCreateView.as_view(), name="actors_list_create" ),
    path('actors/<int:pk>/',ActorsReciveUpdateDeleteView.as_view(), name="actors_details_update_delete" ),
]
