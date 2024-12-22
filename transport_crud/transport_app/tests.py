from django.test import TestCase
from .models import Driver, Vehicle, Route
from datetime import date, datetime

class ModelsTestCase(TestCase):
    def setUp(self):
        # Создание тестового водителя
        self.driver = Driver.objects.create(
            surname="Иванов",
            firstname="Иван",
            lastname="Петрович",
            birthdate=date(1980, 5, 10),
            phone_number="+71234567890",
            license_num="AB1234567",
            license_exp=date(2025, 5, 10),
        )

        # Создание тестового транспортного средства
        self.vehicle = Vehicle.objects.create(
            driver=self.driver,
            brand="Toyota",
            model="Camry",
            release_year=2020,
            serial_number="12345XYZ",
            color="Black",
        )

        # Создание тестового маршрута
        self.route = Route.objects.create(
            driver=self.driver,
            start_location="Москва",
            end_location="Санкт-Петербург",
            distance=700.5,
            start_datetime=datetime(2024, 12, 20, 10, 0, 0),
            end_datetime=datetime(2024, 12, 20, 18, 30, 0),
        )

    def test_driver_creation(self):
        # Проверяем создание водителя
        self.assertEqual(self.driver.surname, "Иванов")
        self.assertEqual(self.driver.phone_number, "+71234567890")

    def test_vehicle_creation(self):
        # Проверяем создание транспортного средства
        self.assertEqual(self.vehicle.brand, "Toyota")
        self.assertEqual(self.vehicle.driver, self.driver)

    def test_route_creation(self):
        # Проверяем создание маршрута
        self.assertEqual(self.route.start_location, "Москва")
        self.assertEqual(self.route.driver, self.driver)

    def test_driver_vehicle_relationship(self):
        # Проверяем связь водителя с транспортным средством
        self.assertEqual(self.driver.vehicles.count(), 1)
        self.assertEqual(self.driver.vehicles.first(), self.vehicle)

    def test_driver_route_relationship(self):
        # Проверяем связь водителя с маршрутом
        self.assertEqual(self.driver.routes.count(), 1)
        self.assertEqual(self.driver.routes.first(), self.route)
