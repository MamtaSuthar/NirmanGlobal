from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from apps.home.views import privacy_policy, terms, blog, single
from apps.projects.views import project_list, project_details, project_filter
from apps.services.views import service_images
from apps.users.views import register_view, CustomLoginView
from apps.contact.views import ai_room_view
from apps.book_desgin.views import book_design

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # Steel & Aluminium site at root
    path('', include('apps.home.steel_urls')),
    path('steel/', RedirectView.as_view(url='/', permanent=False)),

    # Utility / auth routes
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),

    # Service image API (used by steel service detail modal)
    path('service/<int:id>/images/', service_images, name='service_images'),

    # Project routes (used by steel project pages)
    path('project_list/', project_list, name='project_list'),
    path('projects/filter/', project_filter, name='project_filter'),

    # Misc pages
    path('ai-room/', ai_room_view, name='ai_room'),
    path('book-design/', book_design, name='book_design'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms/', terms, name='terms'),
    path('blog/', blog, name='blog'),
    path('blog/single/', single, name='single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
