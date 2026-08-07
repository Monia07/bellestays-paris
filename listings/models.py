from django.conf import settings
from django.db import models


class Listing(models.Model):
    PROPERTY_TYPES = [
        ("Apartment", "Apartment"),
        ("Studio", "Studio"),
        ("Loft", "Loft"),
        ("House", "House"),
    ]

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="listings",
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    district = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default="Apartment",
    )

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    guests = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)

    image = models.URLField(blank=True)

    available = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title