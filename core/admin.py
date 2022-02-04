from django.contrib import admin

from core.models import Service, ServiceItem


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    search_fields = ['name']


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'is_active', 'created_at', 'updated_at']
    list_filter = ['service', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name', 'service']
