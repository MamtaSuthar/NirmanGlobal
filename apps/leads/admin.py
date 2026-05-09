from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('client_name', 'email', 'phone')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
