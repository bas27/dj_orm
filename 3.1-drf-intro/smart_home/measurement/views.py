# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementCreateSerializer, SensorDetailSerializer


class SensorGetCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, pk):
        queryset = Sensor.objects.get(id=pk)
        ser = SensorDetailSerializer(queryset)
        return Response(ser.data)


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

