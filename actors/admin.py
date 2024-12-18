from django.contrib import admin
from actors.models import ActorsModel


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality')
    search_fields = ('name', "nationality")


admin.site.register(ActorsModel, ActorsAdmin)
