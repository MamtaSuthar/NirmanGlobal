from django.contrib import admin
from .models import Service, ServiceImage

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 3

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]