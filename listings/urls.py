from django.urls import path
from . import views

urlpatterns = [
    path("", views.listing_list, name="listing_list"),
    path("add/", views.add_listing, name="add_listing"),
]
