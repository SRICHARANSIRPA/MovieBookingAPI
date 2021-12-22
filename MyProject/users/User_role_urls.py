from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUserRoles.as_view()),
    path('<uuid:pk>/', views.UserRoleDetail.as_view())
]