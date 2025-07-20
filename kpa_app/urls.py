from django.urls import path
from .views import wheel_specification_view

urlpatterns = [
    path('forms/wheel-specifications', wheel_specification_view, name='wheel-specifications'),
]
