from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="Your Name (optional)"
    )

    email = forms.EmailField(
        required=False,
        label="Your Email (optional)"
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=True,
        label="Your Feedback"
    )

    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty"
    )

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("normal", "Normal"),
        ("high", "High"),
    ]

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        initial="normal",
        required=False,
        label="Priority"
    )