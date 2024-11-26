from django.contrib import admin
from movies.models import MovieModel

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'genre', 'release_data', 'resume', )
    search_fields = ('title', 'genre','release_data')
admin.site.register(MovieModel, MovieAdmin)
