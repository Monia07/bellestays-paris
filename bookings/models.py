from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from listings.models import Listing


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    guest_name = models.CharField(
        max_length=100,
    )

    guest_email = models.EmailField()

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(
                1,
                message="At least one guest is required.",
            ),
        ],
    )

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    paid = models.BooleanField(
        default=False,
    )

    stripe_session_id = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.guest_name} - {self.listing.title}"
        )