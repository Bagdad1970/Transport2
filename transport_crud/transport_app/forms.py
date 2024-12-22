from django import forms
from .models import Driver, Vehicle, Route

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['surname', 'firstname', 'lastname', 'birthdate', 'phone_number', 'license_num', 'license_exp']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['driver', 'brand', 'model', 'release_year', 'serial_number', 'color']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['driver', 'start_location', 'end_location', 'distance', 'start_datetime', 'end_datetime']
