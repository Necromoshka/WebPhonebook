from django.urls import path
from .views import index, by_intel


urlpatterns = [
    path('<str:telnum>/',by_intel),
    path('', index),
]
