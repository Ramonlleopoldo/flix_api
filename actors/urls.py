from django.urls import path
from . import views

urlpatterns = [
    path('actors/',views.ActorListCreateView.as_view(), name="actors_list_create" ),
    path('actors/<int:pk>/',views.ActorsReciveUpdateDeleteView.as_view(), name="actors_details_update_delete" ),
]