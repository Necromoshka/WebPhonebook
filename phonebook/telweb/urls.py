from django.urls import path
from .views import index, by_intel, PrCreateView, telCreateView


urlpatterns = [
    path('addTel/', telCreateView.as_view(), name='addTel'),
    path('addPr/', PrCreateView.as_view(), name='addPr'),
    path('<str:telnum>/',by_intel, name='by_intel'),
    path('', index, name='index'),
]
