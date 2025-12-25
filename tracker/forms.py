from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Library
from django.forms.widgets import CheckboxSelectMultiple


class InlineCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = "widgets/inline_checkbox_select.html"


class LibraryForm(forms.ModelForm):
    # User-typed fields
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

    # NEW: Replace year with a real release_date field
    release_date = forms.DateField(
        required=False,
        label="Release Date",
        widget=forms.DateInput(attrs={"type": "date"})
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
            "mediums": InlineCheckboxSelectMultiple(),
            "subscription_services": InlineCheckboxSelectMultiple(),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "finish_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "mediums": "Medium",
            "subscription_services": "Subscription Services",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap classes to all fields
        for name, field in self.fields.items():
            widget = field.widget

            # Multi-checkbox fields
            if isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs.update({"class": "form-check"})
                continue

            # Dropdowns
            if isinstance(widget, forms.Select):
                widget.attrs.update({"class": "form-select"})
                continue

            # Everything else (text, number, date, textarea)
            widget.attrs.update({"class": "form-control"})

        # Add HTML limits for priority
        self.fields["priority"].widget.attrs.update({
            "min": 1,
            "max": 10
        })


# Registration Form

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})