from django.shortcuts import render, redirect, get_object_or_404

from listings.models import Listing
from .models import Booking
from .forms import BookingForm


def create_booking(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.listing = listing
            booking.save()

            return redirect("booking_success")

    else:
        form = BookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {
            "listing": listing,
            "form": form,
        },
    )


def booking_success(request):
    return render(
        request,
        "bookings/booking_success.html",
    )