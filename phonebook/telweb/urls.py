from django.urls import path
from .views import index, by_intel, PrCreateView


urlpatterns = [
    path('add/', PrCreateView.as_view(), name='add'),
    path('<str:telnum>/',by_intel, name='by_intel'),
    path('', index, name='index'),
]
