from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .forms import BookingForm


def book_design(request):
    if request.method == "POST":

        # ✅ Check terms acceptance
        if not request.POST.get("terms"):
            messages.error(request, "Please accept Terms & Conditions.")
            return redirect("/")

        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            # 📩 Email to Admin
            subject_admin = "New 3D/4D Design Booking"
            message_admin = f"""
New Booking Received:

Name: {booking.name}
Phone: {booking.phone}
Email: {booking.email}
Service: {booking.service_type}
Date: {booking.date}
Time: {booking.time}

Message:
{booking.message}
"""

            subject_user = "Booking Received - We’ll Contact You Soon"

            try:
                # Send to admin
                send_mail(
                    subject_admin,
                    message_admin,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )

                # Send email to user
                if booking.email:
                    html_content = render_to_string(
                        "emails/booking_confirmation.html",
                        {
                            "name": booking.name,
                            "service": booking.service_type,
                            "date": booking.date,
                            "time": booking.time,
                            "project_name": settings.PROJECT_NAME,
                        },
                    )

                    email = EmailMultiAlternatives(
                        subject_user,
                        "",
                        settings.DEFAULT_FROM_EMAIL,
                        [booking.email],
                    )
                    email.attach_alternative(html_content, "text/html")
                    email.send()

            except Exception as e:
                print("Email error:", e)

            messages.success(request, "Booking submitted successfully!")

        else:
            messages.error(request, "Please fill all required fields correctly.")

    return redirect("/")