from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.index),
    path('index', controller.api_index),
]
