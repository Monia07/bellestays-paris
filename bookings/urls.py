from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/<int:listing_id>/",
        views.create_booking,
        name="create_booking",
    ),
    path(
        "success/",
        views.booking_success,
        name="booking_success",
    ),
    path(
        "",
        views.booking_list,
        name="booking_list",
    ),
]