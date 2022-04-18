from rest_framework import serializers

from measurement.models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]


class MeasurementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        sensor = SensorSerializer()
        model = Measurement
        fields = ['sensor', 'temperature']

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        sensor = SensorSerializer()
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
