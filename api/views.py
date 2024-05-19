from rest_framework import viewsets
from .models import Equipment, Data, Alert
from .serializers import EquipmentSerializer, DataSerializer, AlertSerializer
from rest_framework.permissions import IsAuthenticated

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]


from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'api.views.custom_exception_handler',
}
