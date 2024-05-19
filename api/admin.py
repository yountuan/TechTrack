from django.contrib import admin
from .models import Data, Equipment, Alert

# Register your models here.
admin.site.register(Data)
admin.site.register(Alert)
admin.site.register(Equipment)