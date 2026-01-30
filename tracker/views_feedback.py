from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from .forms_feedback import FeedbackForm
from django.conf import settings
from .models_feedback import Feedback
from django.shortcuts import render

@require_POST
def submit_feedback(request):
    form = FeedbackForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data.get("name") or "Anonymous"
        email = form.cleaned_data.get("email") or "No email provided"
        message = form.cleaned_data["message"]
        priority = form.cleaned_data.get("priority") or "normal"

        # Honeypot check
        if form.cleaned_data.get("honeypot"):
            return JsonResponse({"success": True})  # Pretend success, silently ignore

        # Save to database
        Feedback.objects.create(
            name=name if name != "Anonymous" else "",
            email=email if email != "No email provided" else "",
            message=message,
            priority=priority,
        )

        # Build email
        full_message = (
            f"New feedback submitted on Backlogged.uk\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Priority: {priority.capitalize()}\n\n"
            f"Message:\n{message}"
        )

        # Send email
        send_mail(
            subject="New Backlogged.uk Feedback",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        # Send confirmation email to the user (if they provided an email)
        if email != "No email provided":
            send_mail(
                subject="Thanks for your feedback",
                message=(
                    "Hi,\n\n"
                    "Thanks for taking the time to send feedback about Backlogged.uk.\n"
                    "I really appreciate it.\n\n"
                    "— Meta1ingus"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )

        return JsonResponse({"success": True})

    # Invalid form
    return JsonResponse({"success": False, "errors": form.errors}, status=400)

def feedback_dashboard(request):
    feedback_list = Feedback.objects.order_by("-submitted_at")
    return render(request, "tracker/feedback_dashboard.html", {"feedback_list": feedback_list})
