from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from listings.models import Listing
from .models import Booking
from .forms import BookingForm


@login_required
def create_booking(request, listing_id):
    listing = get_object_or_404(
        Listing,
        pk=listing_id,
    )

    if request.method == "POST":
        form = BookingForm(request.POST)
        form.listing = listing

        if form.is_valid():
            booking = form.save(commit=False)
            booking.listing = listing
            booking.guest = request.user
            booking.save()

            return redirect("booking_success")

    else:
        form = BookingForm()
        form.listing = listing

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


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(
        guest=request.user
    ).order_by("-created_at")

    return render(
        request,
        "bookings/booking_list.html",
        {
            "bookings": bookings,
        },
    )


@login_required
def my_bookings(request):
    return booking_list(request)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        guest=request.user,
    )

    if request.method == "POST":
        booking.delete()
        return redirect("my_bookings")

    return render(
        request,
        "bookings/delete_booking.html",
        {
            "booking": booking,
        },
    )