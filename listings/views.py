from django.shortcuts import render, redirect, get_object_or_404

from .models import Listing
from .forms import ListingForm


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


def add_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save()
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