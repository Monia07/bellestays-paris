from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "listing",
        "guest",
        "guest_name",
        "guest_email",
        "check_in",
        "check_out",
        "created_at",
    )

    list_filter = (
        "check_in",
        "check_out",
        "created_at",
    )

    search_fields = (
        "guest_name",
        "guest_email",
        "listing__title",
        "guest__username",
    )
