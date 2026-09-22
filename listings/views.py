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
def my_listings(request):
    listings = Listing.objects.filter(
        host=request.user
    ).order_by("-created_on")

    return render(
        request,
        "listings/my_listings.html",
        {
            "listings": listings,
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

            return redirect("my_listings")

    else:
        form = ListingForm()

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
        },
    )


@login_required
def edit_listing(request, pk):
    listing = get_object_or_404(
        Listing,
        pk=pk,
        host=request.user,
    )

    if request.method == "POST":
        form = ListingForm(
            request.POST,
            instance=listing,
        )

        if form.is_valid():
            updated_listing = form.save(commit=False)
            updated_listing.host = request.user
            updated_listing.save()

            return redirect("my_listings")

    else:
        form = ListingForm(instance=listing)

    return render(
        request,
        "listings/add_listing.html",
        {
            "form": form,
        },
    )


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(
        Listing,
        pk=pk,
        host=request.user,
    )

    if request.method == "POST":
        listing.delete()
        return redirect("my_listings")

    return render(
        request,
        "listings/delete_listing.html",
        {
            "listing": listing,
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