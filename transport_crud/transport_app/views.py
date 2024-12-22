from django.shortcuts import render, redirect, get_object_or_404
from .forms import DriverForm, RouteForm, VehicleForm
from .models import Driver, Vehicle, Route

def home(request):
    return render(request, 'home.html')

# Представление для отображения записей водителей
def drivers_list(request):
    drivers = Driver.objects.all()  # Получаем всех водителей
    return render(request, 'drivers_list.html', {'drivers': drivers})

# Представление для отображения записей автомобилей
def vehicles_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles_list.html', {'vehicles': vehicles})

# Представление для отображения маршрутов
def routes_list(request):
    routes = Route.objects.all()
    return render(request, 'routes_list.html', {'routes': routes})

# Представление для добавления нового водителя
def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую запись
            return redirect('drivers_list')  # Перенаправляем на страницу списка водителей
    else:
        form = DriverForm()

    return render(request, 'add_driver.html', {'form': form})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles_list')
    else:
        form = VehicleForm()

    return render(request, 'add_vehicle.html', {'form': form})

# Представление для добавления нового маршрута
def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routes_list')
    else:
        form = RouteForm()

    return render(request, 'add_route.html', {'form': form})

def model_action(request, model_name):
    # Определяем модель и форму для нее
    if model_name == 'drivers':
        form = DriverForm()
        list_url = 'drivers_list'
        add_url = 'add_driver'
    elif model_name == 'vehicles':
        form = VehicleForm()
        list_url = 'vehicles_list'
        add_url = 'add_vehicle'
    elif model_name == 'routes':
        form = RouteForm()
        list_url = 'routes_list'
        add_url = 'add_route'
    else:
        return redirect('home')

    return render(request, 'model_action.html', {
        'model_name': model_name,
        'form': form,
        'list_url': list_url,
        'add_url': add_url
    })

# Представление для просмотра деталей водителя
def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'driver_detail.html', {'driver': driver})

# Представление для просмотра деталей автомобиля
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

# Представление для просмотра деталей маршрута
def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'route_detail.html', {'route': route})

def edit_driver(request, pk):
    driver = get_object_or_404(Driver, pk=pk)  # Получаем водителя по pk
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('drivers_list')  # Перенаправляем на список водителей
    else:
        form = DriverForm(instance=driver)  # Заполняем форму данными водителя

    return render(request, 'edit_driver.html', {'form': form, 'driver': driver})

# Представление для редактирования автомобиля
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)  # Получаем автомобиль по pk
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('vehicles_list')  # Перенаправляем на список автомобилей
    else:
        form = VehicleForm(instance=vehicle)  # Заполняем форму данными автомобиля

    return render(request, 'edit_vehicle.html', {'form': form, 'vehicle': vehicle})

# Представление для редактирования маршрута
def edit_route(request, pk):
    route = get_object_or_404(Route, pk=pk)  # Получаем маршрут по pk
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('routes_list')  # Перенаправляем на список маршрутов
    else:
        form = RouteForm(instance=route)  # Заполняем форму данными маршрута

    return render(request, 'edit_route.html', {'form': form, 'route': route})