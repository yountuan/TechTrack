from django.test import TestCase
from .models import Equipment, Data, Alert

class EquipmentTestCase(TestCase):
    def setUp(self):
        Equipment.objects.create(equipment_type="Robot", model="R100", installation_date="2022-01-01", status="Active")

    def test_equipment_creation(self):
        equipment = Equipment.objects.get(model="R100")
        self.assertEqual(equipment.equipment_type, "Robot")

class DataTestCase(TestCase):
    def setUp(self):
        self.equipment = Equipment.objects.create(equipment_type="Robot", model="R100", installation_date="2022-01-01", status="Active")
        Data.objects.create(equipment=self.equipment, temperature=75.5, speed=150.0, pressure=1.2)

    def test_data_creation(self):
        data = Data.objects.get(equipment=self.equipment)
        self.assertEqual(data.temperature, 75.5)
        self.assertEqual(data.speed, 150.0)
        self.assertEqual(data.pressure, 1.2)
        self.assertEqual(data.equipment.model, "R100")

class AlertTestCase(TestCase):
    def setUp(self):
        self.equipment = Equipment.objects.create(equipment_type="Robot", model="R100", installation_date="2022-01-01", status="Active")
        Alert.objects.create(equipment=self.equipment, description="High temperature detected")

    def test_alert_creation(self):
        alert = Alert.objects.get(equipment=self.equipment)
        self.assertEqual(alert.description, "High temperature detected")
        self.assertEqual(alert.equipment.model, "R100")
