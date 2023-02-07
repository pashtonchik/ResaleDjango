from django.urls import path
from rest_framework import routers

from .api import *

router = routers.DefaultRouter()

urlpatterns = [
    path('api/create/order/', create_order),
] + router.urls