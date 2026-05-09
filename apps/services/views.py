from django.shortcuts import render
from .models import Service
from django.conf import settings
from django.http import JsonResponse
from apps.site_settings.models import SiteSettings

def service(request):
    services = Service.objects.prefetch_related("images").all()

    return render(request, 'service.html', {'services': services, 'PROJECT_NAME': settings.PROJECT_NAME})

def service_details(request):
    site_settings = SiteSettings.objects.first()
    services = Service.objects.prefetch_related("images").all()
    
    return render(request, 'service_details.html', {'site_settings' : site_settings,
                                                    'services': services, 
                                                    'PROJECT_NAME': settings.PROJECT_NAME})


def service_images(request, id):
    service = Service.objects.get(id=id)

    images = []
    for img in service.images.all():
        try:
            images.append(request.build_absolute_uri(img.image.url))
        except Exception:
            continue

    return JsonResponse({"images": images})