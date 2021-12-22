from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListRoles.as_view()),
    path('<uuid:pk>/', views.RoleDetail.as_view())
]