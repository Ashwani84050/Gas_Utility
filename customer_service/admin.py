from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
 
#admin.site.register(Customer, CustomerAdmin)   

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'submitted_at', 'resolved_at')
