from django import forms
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
    guests = forms.TypedChoiceField(
        label="Number of guests",
        coerce=int,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    class Meta:
        model = Booking

        exclude = [
            "listing",
            "guest",
            "created_at",
        ]

        widgets = {
            "guest_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your name",
                }
            ),
            "check_in": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "check_out": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        self.listing = kwargs.pop("listing", None)
        super().__init__(*args, **kwargs)

        self.fields.pop("guest_email")

        if self.listing:
            self.fields["guests"].choices = [
                (
                    i,
                    f"{i} guest" if i == 1 else f"{i} guests",
                )
                for i in range(
                    1,
                    self.listing.guests + 1,
                )
            ]

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_in < timezone.localdate():
            raise forms.ValidationError(
                "Check-in date cannot be in the past."
            )

        if check_in and check_out:

            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )

            overlapping_booking = Booking.objects.filter(
                listing=self.listing,
                check_in__lt=check_out,
                check_out__gt=check_in,
            ).exists()

            if overlapping_booking:
                raise forms.ValidationError(
                    "These dates are already booked. "
                    "Please choose different dates."
                )

        return cleaned_data