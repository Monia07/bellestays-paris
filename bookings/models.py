from django.db import models
from listings.models import Listing


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    guest_name = models.CharField(max_length=100)

    guest_email = models.EmailField()

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.listing.title}"