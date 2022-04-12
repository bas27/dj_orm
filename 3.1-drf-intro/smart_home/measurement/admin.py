from xml.dom.pulldom import parseString
from django.contrib import admin

from measurement.models import Measurement, Sensor

# Register your models here.
@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    pass
    
@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    pass