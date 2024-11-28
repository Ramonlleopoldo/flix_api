from django.urls import path
from . import views


urlpatterns=[ path('genres/', views.GenreListCreateView.as_view(), name= 'genres_list_create'),
path('genres/<int:pk>/',views.GenreRetriveUpdateDelete.as_view(), name='genre_detail_update_delete'),]
