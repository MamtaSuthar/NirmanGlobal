from django.urls import path
from . import steel_views

urlpatterns = [
    path('',                          steel_views.steel_home,           name='steel_home'),
    path('about/',                    steel_views.steel_about,          name='steel_about'),
    path('services/',                 steel_views.steel_services,       name='steel_services'),
    path('services/<int:service_id>/',steel_views.steel_service_detail, name='steel_service_detail'),
    path('projects/',                 steel_views.steel_projects,       name='steel_projects'),
    path('projects/<slug:slug>/',     steel_views.steel_project_detail, name='steel_project_detail'),
    path('contact/',                  steel_views.steel_contact,        name='steel_contact'),
    path('quote/',                    steel_views.steel_quote,          name='steel_quote'),
]
