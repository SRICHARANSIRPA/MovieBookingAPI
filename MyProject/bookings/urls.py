from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBookings.as_view()),
    path('<uuid:pk>/', views.ListBooking.as_view())
]
