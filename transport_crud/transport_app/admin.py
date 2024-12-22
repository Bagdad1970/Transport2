from django.contrib import admin
from .models import Driver, Vehicle, Route

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'lastname', 'phone_number', 'license_num', 'license_exp')
    list_filter = ('birthdate', 'license_exp')
    search_fields = ('surname', 'firstname', 'lastname', 'phone_number', 'license_num')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'release_year', 'serial_number', 'color', 'driver')
    list_filter = ('release_year', 'color')
    search_fields = ('brand', 'model', 'serial_number')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'end_location', 'distance', 'start_datetime', 'end_datetime', 'driver')
    list_filter = ('start_datetime', 'end_datetime', 'driver')
    search_fields = ('start_location', 'end_location')
    ordering = ('-distance',)
