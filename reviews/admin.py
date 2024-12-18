from django.contrib import admin
from reviews.models import ReviewModels


@admin.register(ReviewModels)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'rating', 'coments')
    search_fields = ('user_name',)
