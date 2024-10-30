from .views import *
from django.urls import path

urlpatterns = [
    path('api/read-history/', ReadHistoryAPIView.as_view(), name='api-read-history'),
]