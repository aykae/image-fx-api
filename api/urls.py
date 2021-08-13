from django.urls import include, path
from rest_framework import routers
from .views import *

app_name = 'api'
urlpatterns = [
    path('grayscale/', grayscale),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]