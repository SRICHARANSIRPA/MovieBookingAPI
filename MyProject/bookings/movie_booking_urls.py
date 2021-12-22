from django.urls import path

from .views import *

urlpatterns = [
    path('',MovieBooking.as_view())
]
