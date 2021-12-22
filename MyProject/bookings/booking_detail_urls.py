from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBookingDetails.as_view()),
    path('<uuid:pk>/', views.ListBookingDetail.as_view())
]
