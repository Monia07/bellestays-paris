from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def listing_list(request):
    listings = Listing.objects.all()

    return render(request, "listings/listing_list.html", {
        "listings": listings
    })


def add_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("listing_list")

    else:
        form = ListingForm()

    return render(request, "listings/add_listing.html", {
        "form": form
    })