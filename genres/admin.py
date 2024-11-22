from django.contrib import admin
from genres.models import GenresModel

class GenresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(GenresModel, GenresAdmin)
