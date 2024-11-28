from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='reviews_list_create'),
    path('reviews/<int:pk>/', views.ReviewRestriveUpdateDeleteView.as_view(), name='reviews_details_update_delete')
]