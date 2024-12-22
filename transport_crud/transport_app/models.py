from django.db import models

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)  # Автоматический ID
    surname = models.CharField(max_length=40, null=False)
    firstname = models.CharField(max_length=40, null=False)
    lastname = models.CharField(max_length=100, null=True, blank=True)  # NULL разрешен
    birthdate = models.DateField(null=False)
    phone_number = models.CharField(max_length=20, unique=True, null=False)
    license_num = models.CharField(max_length=20, unique=True, null=False)
    license_exp = models.DateField(null=False)

    def __str__(self):
        return f"{self.surname} {self.firstname}"


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)  # Автоматический ID
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="vehicles")  # Внешний ключ на Driver
    brand = models.CharField(max_length=40, null=False)
    model = models.CharField(max_length=40, null=False)
    release_year = models.IntegerField(null=False)
    serial_number = models.CharField(unique=True, null=False, max_length=10)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)  # Автоматический ID
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="routes")  # Внешний ключ на Driver
    start_location = models.CharField(max_length=100, null=False)
    end_location = models.CharField(max_length=100, null=False)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # NULL разрешен
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)

    def __str__(self):
        return f"Route {self.route_id} by {self.driver}"
