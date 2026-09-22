from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForm, SignUpForm


def listing_list(request):
    listings = Listing.objects.all()

    return render(
        request,
        "listings/listing_list.html",
        {
            "listings": listings,
        },
    )


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)

    return render(
        request,
        "listings/listing_detail.html",
        {
            "listing": listing,
        },
    )


@login_required
def add_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = request.user
            listing.save()

            return redirect("listing_list")

    else:
        form = ListingForm()

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
        },
    )


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("listing_list")

    else:
        form = SignUpForm()

    return render(
        request,
        "registration/signup.html",
        {
            "form": form,
        },
    )