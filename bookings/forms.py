from django import forms
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
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
            "guest_email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
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
            "guests": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
        }

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