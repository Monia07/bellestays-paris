from django.urls import path
from . import views

urlpatterns = [
    path("", views.listing_list, name="listing_list"),
    path("add/", views.add_listing, name="add_listing"),
    path("<int:pk>/", views.listing_detail, name="listing_detail"),
]