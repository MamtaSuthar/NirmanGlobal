from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from apps.services.models import Service
from apps.projects.models import Project, Category
from apps.team.models import TeamMember
from apps.testimonials.models import Testimonial
from apps.site_settings.models import SiteSettings
from apps.contact.models import Contact
from apps.leads.models import Lead


def _ctx(request):
    """Shared context injected into every steel view."""
    return {
        'site_settings': SiteSettings.objects.first(),
        'PROJECT_NAME': getattr(settings, 'PROJECT_NAME', 'Nirman Global'),
    }


# ── Read-only pages ────────────────────────────────────────────────────────

def steel_home(request):
    ctx = _ctx(request)
    ctx.update({
        'services': Service.objects.all()[:6],
        'featured_projects': Project.objects.filter(is_featured=True, is_active=True)[:6],
        'testimonials': Testimonial.objects.filter(is_active=True),
    })
    return render(request, 'steel/index.html', ctx)


def steel_about(request):
    ctx = _ctx(request)
    ctx.update({
        'team_members': TeamMember.objects.filter(is_active=True),
    })
    return render(request, 'steel/about.html', ctx)


def steel_services(request):
    ctx = _ctx(request)
    ctx.update({'services': Service.objects.all()})
    return render(request, 'steel/services.html', ctx)


def steel_service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    ctx = _ctx(request)
    ctx.update({
        'service': service,
        'all_services': Service.objects.all(),
    })
    return render(request, 'steel/service_detail.html', ctx)


def steel_projects(request):
    ctx = _ctx(request)
    ctx.update({
        'projects': Project.objects.filter(is_active=True).select_related('category'),
        'categories': Category.objects.filter(is_active=True),
    })
    return render(request, 'steel/projects.html', ctx)


def steel_project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    ctx = _ctx(request)
    ctx.update({'project': project})
    return render(request, 'steel/project_detail.html', ctx)


# ── Forms ──────────────────────────────────────────────────────────────────

def steel_contact(request):
    ctx = _ctx(request)

    if request.method == 'POST':
        name     = request.POST.get('name', '').strip()
        email    = request.POST.get('email', '').strip()
        subject  = request.POST.get('subject', '').strip()
        message  = request.POST.get('message', '').strip()
        category = request.POST.get('category', 'general')

        # Validate required fields
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not subject:
            errors['subject'] = 'Subject is required.'
        if not message:
            errors['message'] = 'Message is required.'

        if errors:
            ctx['errors'] = errors
            ctx['form_data'] = request.POST
            return render(request, 'steel/contact.html', ctx)

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            category=category,
        )

        # Notify admin by email (silent fail so form still works if email is misconfigured)
        try:
            send_mail(
                subject=f"[Steel Site] New Contact: {subject}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Category: {category}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(request, 'Your message has been sent! We will get back to you within 24 hours.')
        return redirect('steel_contact')

    return render(request, 'steel/contact.html', ctx)


def steel_quote(request):
    ctx = _ctx(request)

    if request.method == 'POST':
        client_name = request.POST.get('client_name', '').strip()
        email       = request.POST.get('email', '').strip()
        phone       = request.POST.get('phone', '').strip()
        description = request.POST.get('description', '').strip()

        # Validate
        errors = {}
        if not client_name:
            errors['client_name'] = 'Full name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not phone:
            errors['phone'] = 'Phone number is required.'
        if not description:
            errors['description'] = 'Project description is required.'

        if errors:
            ctx['errors'] = errors
            ctx['form_data'] = request.POST
            return render(request, 'steel/quote.html', ctx)

        # Save lead
        Lead.objects.create(
            client_name=client_name,
            email=email,
            phone=phone,
            description=description,
            status='new',
        )

        # Notify admin
        try:
            send_mail(
                subject=f"[Steel Site] New Quote Request from {client_name}",
                message=(
                    f"Name: {client_name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Project Description:\n{description}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(request, 'Quote request submitted! Our team will contact you within 24 hours.')
        return redirect('steel_quote')

    return render(request, 'steel/quote.html', ctx)
