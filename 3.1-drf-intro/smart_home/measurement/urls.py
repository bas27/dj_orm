from django.urls import path

from measurement.views import MeasurementCreate, SensorCreate, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    
    path('sensors/', SensorCreate.as_view()),
    # path('sensors/<int:pk>/', SensorCreate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
]