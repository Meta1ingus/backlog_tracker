# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Library

# Fixed year range: 1980–2030
YEAR_CHOICES = [(y, y) for y in range(2030, 1980 - 1, -1)]

class LibraryForm(forms.ModelForm):
    # New user-typed fields
    title = forms.CharField(
        max_length=200,
        label="Game Title",
        required=True
    )

    edition_name = forms.CharField(
        max_length=200,
        label="Edition Name",
        required=False  # Blank becomes "Standard"
    )

    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        label="Release Year",
        required=True
    )

    class Meta:
        model = Library
        fields = [
            "platform",
            "status",
            "priority",
            "hours_played",
            "notes",
            "start_date",
            "finish_date",
            "mediums",
            "subscription_services",
        ]
        widgets = {
            "mediums": forms.CheckboxSelectMultiple(),
            "subscription_services": forms.CheckboxSelectMultiple(),
        }
        labels = {
            "mediums": "Medium",
            "subscription_services": "Subscription Services",
        }


# Registration Form

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]