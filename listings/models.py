from django.db import models


class Listing(models.Model):
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title