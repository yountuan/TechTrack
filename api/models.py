from django.db import models

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.equipment_type} - {self.model}'

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    speed = models.FloatField()
    pressure = models.FloatField()

    def __str__(self):
        return f'Data for {self.equipment} at {self.timestamp}'

class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='alerts', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'Alert for {self.equipment} at {self.timestamp}'
