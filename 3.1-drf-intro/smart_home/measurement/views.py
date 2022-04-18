from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementCreateSerializer, SensorDetailSerializer, SensorSerializer
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
    serializer_class = MeasurementCreateSerializer
    
    
class SensorDetailView(ListAPIView):
    # queryset = Sensor.objects.all()
    # serializer_class = SensorDetailSerializer
    
    def list(self, request, pk):
       
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(queryset, many=True)
        return Response(serializer.data)