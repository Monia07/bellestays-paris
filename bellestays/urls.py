from django.contrib import admin
from django.urls import path, include

from listings import views as listing_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("listings.urls")),
    path("bookings/", include("bookings.urls")),

    path(
        "accounts/",
        include("django.contrib.auth.urls"),
    ),

    path(
        "accounts/signup/",
        listing_views.signup,
        name="signup",
    ),
]