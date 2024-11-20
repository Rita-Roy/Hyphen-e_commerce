from django.contrib import admin
from .models import Hairstylist, Hairstyle, Appointment

class HairstylistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'experience_years', 'specialization')
    search_fields = ('name', 'specialization')
    list_filter = ('experience_years',)

class HairstyleAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'duration_minutes', 'hairstyle_type', 'created_by','images')
    search_fields = ('name',)
    list_filter = ('hairstyle_type', 'created_by')
    autocomplete_fields = ('created_by',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'stylist', 'hairstyle', 'appointment_date')
    search_fields = ('customer_username', 'stylistname', 'hairstyle_name')
    list_filter = ('appointment_date', 'stylist', 'hairstyle')
    date_hierarchy = 'appointment_date'

admin.site.register(Hairstylist, HairstylistAdmin)
admin.site.register(Hairstyle, HairstyleAdmin)
admin.site.register(Appointment, AppointmentAdmin)