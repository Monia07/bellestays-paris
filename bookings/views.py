from decimal import Decimal

import stripe

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from listings.models import Listing
from .forms import BookingForm
from .models import Booking


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_booking(request, listing_id):
    listing = get_object_or_404(
        Listing,
        pk=listing_id,
    )

    if request.method == "POST":
        form = BookingForm(
            request.POST,
            listing=listing,
        )

        if form.is_valid():
            booking = form.save(commit=False)
            booking.listing = listing
            booking.guest = request.user
            booking.guest_email = request.user.email

            nights = (
                booking.check_out - booking.check_in
            ).days

            total_price = (
                Decimal(nights)
                * listing.price_per_night
            )

            booking.price_per_night = (
                listing.price_per_night
            )
            booking.total_price = total_price
            booking.paid = False

            booking.save()

            domain = (
                request.build_absolute_uri("/")[:-1]
            )

            checkout_session = stripe.checkout.Session.create(
                mode="payment",
                client_reference_id=str(
                    booking.id
                ),
                success_url=(
                    domain
                    + reverse("booking_success")
                    + "?session_id={CHECKOUT_SESSION_ID}"
                ),
                cancel_url=(
                    domain
                    + reverse("booking_cancel")
                ),
                line_items=[
                    {
                        "price_data": {
                            "currency": "eur",
                            "product_data": {
                                "name": listing.title,
                            },
                            "unit_amount": int(
                                total_price * 100
                            ),
                        },
                        "quantity": 1,
                    }
                ],
            )

            booking.stripe_session_id = (
                checkout_session.id
            )
            booking.save()

            return redirect(
                checkout_session.url,
                code=303,
            )

    else:
        form = BookingForm(
            listing=listing,
        )

    return render(
        request,
        "bookings/create_booking.html",
        {
            "listing": listing,
            "form": form,
        },
    )


def booking_success(request):
    booking = None

    session_id = request.GET.get("session_id")

    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(
                session_id
            )

            if session.payment_status == "paid":
                booking = Booking.objects.get(
                    stripe_session_id=session.id
                )

                booking.paid = True
                booking.save()

        except Exception:
            booking = None

    return render(
        request,
        "bookings/booking_success.html",
        {
            "booking": booking,
        },
    )


def booking_cancel(request):
    return render(
        request,
        "bookings/booking_cancel.html",
    )


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(
        guest=request.user,
    ).order_by(
        "-created_at",
    )

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

        return redirect(
            "my_bookings",
        )

    return render(
        request,
        "bookings/delete_booking.html",
        {
            "booking": booking,
        },
    )

