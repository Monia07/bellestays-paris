from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing

        exclude = [
            "host",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Property title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your property",
                }
            ),
            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Street address",
                }
            ),
            "property_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "price_per_night": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Price per night",
                }
            ),
            "guests": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "bedrooms": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "bathrooms": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "image": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Image URL",
                }
            ),
            "available": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Choose a username",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Create a password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm your password",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]