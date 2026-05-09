# views.py
from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from apps.site_settings.models import SiteSettings

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{'projects':projects, 'PROJECT_NAME': settings.PROJECT_NAME})

def project_filter(request):
    status = request.GET.get("status")

    projects = Project.objects.all()

    if status:
        projects = projects.filter(status__iexact=status)

    html = render_to_string(
        "projects/project_items.html",
        {"projects": projects},
        request=request
    )

    return JsonResponse({"html": html})

def project_list(request):
    site_settings = SiteSettings.objects.first()
    status = request.GET.get('status')

    projects = Project.objects.all().order_by('-created_at')

    if status:
        projects = projects.filter(status=status)

    categories = Category.objects.filter(is_active=True)

    context = {
        'projects': projects,
        'categories': categories,
        'active_status': status,
        'site_settings' : site_settings,
    }
    return render(request, 'projects/project_list.html', context)


def project_details(request, slug):
    site_settings = SiteSettings.objects.first()
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'site_settings' : site_settings
    })