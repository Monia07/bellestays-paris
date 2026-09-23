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
        "cancel/",
        views.booking_cancel,
        name="booking_cancel",
    ),

    path(
        "",
        views.booking_list,
        name="booking_list",
    ),

    path(
        "my-bookings/",
        views.my_bookings,
        name="my_bookings",
    ),

    path(
        "delete/<int:booking_id>/",
        views.delete_booking,
        name="delete_booking",
    ),
]