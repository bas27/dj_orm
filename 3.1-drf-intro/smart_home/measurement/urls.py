from django.urls import path

from measurement.views import SensorGetCreate, SensorDetailUpdate, MeasurementCreate
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('sensors/', SensorGetCreate.as_view()),
    path('sensors/<int:pk>/', SensorDetailUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
