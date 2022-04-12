from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorCreate(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
# class SensorUpdate(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
    
    
class MeasurementCreate(CreateAPIView):
    
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
    def create(self, serializer):
        sensor_id = get_object_or_404(Sensor, id=self.request.data.get(id='sensor'))
        return serializer.save(sensor=sensor_id)
    
    
class SensorDetailView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer