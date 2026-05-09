from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from apps.site_settings.models import SiteSettings
from apps.ai_engine.utils import detect_category, generate_ai_response, ask_gemini, generate_room_design

def contact_view(request):
    site_settings = SiteSettings.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            # 🧠 AI Category
            contact.category = detect_category(contact.message)

            # 🧠 AI Suggestion
            # ai_reply = generate_ai_response(contact.message)
            ai_reply = ask_gemini(contact.message)
            if hasattr(contact, 'ai_response'):
                contact.ai_response = ai_reply

            contact.save()

            # 📧 Admin Email
            admin_subject = f"New Contact: {contact.subject}"
            admin_message = f"""
Name: {contact.name}
Email: {contact.email}
Category: {contact.category}

Message:
{contact.message}

AI Suggestion:
{ai_reply}
            """

            send_mail(
                admin_subject,
                admin_message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # 📧 User Email
            user_subject = "Interior Design Suggestions for You"
            user_message = f"""
Hi {contact.name},

Thanks for reaching out! 😊

Based on your request:
"{contact.subject}"

Here are some suggestions:

{ai_reply}

Our team will contact you shortly.

Best regards,  
Interior Design Team
            """

            send_mail(
                user_subject,
                user_message,
                settings.ADMIN_EMAIL,
                [contact.email],
                fail_silently=False,
            )

            # ✅ STORE AI RESPONSE FOR UI
            request.session['ai_reply'] = ai_reply

            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'contact.html', {'form': form,
            'site_settings' : site_settings})

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form,
    'site_settings' : site_settings})

def contact_success(request):
    ai_reply = request.session.get('ai_reply', None)
    return render(request, 'contact.html', {'ai_reply': ai_reply})

def ai_room_view(request):
    result = None
    site_settings = SiteSettings.objects.first()
    if request.method == "POST":
        room = request.POST.get("room")
        budget = request.POST.get("budget")
        style = request.POST.get("style")

        result = generate_room_design(room, budget, style)

    return render(request, "ai_room.html", {"result": result,
                                            'site_settings' : site_settings,})