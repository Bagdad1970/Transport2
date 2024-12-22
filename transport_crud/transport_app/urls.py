from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('model_action/<str:model_name>/', views.model_action, name='model_action'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('add_route/', views.add_route, name='add_route'),
    path('drivers/', views.drivers_list, name='drivers_list'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('routes/', views.routes_list, name='routes_list'),
    path('driver/<int:pk>/', views.driver_detail, name='driver_detail'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('route/<int:pk>/', views.route_detail, name='route_detail'),
]
