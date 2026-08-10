from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = [
            "guest_name",
            "guest_email",
            "check_in",
            "check_out",
            "guests",
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