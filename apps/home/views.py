from django.conf import settings
from django.shortcuts import render
from apps.site_settings.models import SiteSettings


def privacy_policy(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'privacy_policy.html', {
        'site_settings': site_settings,
        'PROJECT_NAME': settings.PROJECT_NAME,
    })


def terms(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'terms.html', {
        'site_settings': site_settings,
        'PROJECT_NAME': settings.PROJECT_NAME,
    })


def blog(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'blog.html', {
        'site_settings': site_settings,
        'PROJECT_NAME': settings.PROJECT_NAME,
    })


def single(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'single.html', {
        'site_settings': site_settings,
        'PROJECT_NAME': settings.PROJECT_NAME,
    })
