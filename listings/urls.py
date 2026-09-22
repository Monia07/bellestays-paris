from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.listing_list,
        name="listing_list",
    ),

    path(
        "add/",
        views.add_listing,
        name="add_listing",
    ),

    path(
        "my-listings/",
        views.my_listings,
        name="my_listings",
    ),

    path(
        "<int:pk>/edit/",
        views.edit_listing,
        name="edit_listing",
    ),

    path(
        "<int:pk>/delete/",
        views.delete_listing,
        name="delete_listing",
    ),

    path(
        "<int:pk>/",
        views.listing_detail,
        name="listing_detail",
    ),
]