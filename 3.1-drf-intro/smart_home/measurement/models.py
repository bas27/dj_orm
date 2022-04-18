from django.db import models
from django.forms import CharField

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.CharField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name
class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.CharField(max_length=10, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta():
        verbose_name = 'Показание температуры'
        verbose_name_plural = 'Показания температуры'