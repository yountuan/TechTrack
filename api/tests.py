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
        equipment = Equipment.objects.create(equipment_type="Robot", model="R100", installation_date="2022-01-01", status="Active")
        Data.objects.create(equipment=equipment, temperature=75.5, speed=150.0, pressure=1.2)
