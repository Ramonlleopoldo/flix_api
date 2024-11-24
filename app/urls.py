
from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView,GenreRetriveUpdateDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateView.as_view(), name= 'genres_created_list'),
    path('genres/<int:pk>/',GenreRetriveUpdateDelete.as_view(), name='genre_detail'),
]
