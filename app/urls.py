
from django.contrib import admin
from django.urls import path
from genres.views import genres_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genres_list_view, name= 'genres')
]
