from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUsers.as_view()),
    path('<uuid:pk>/', views.UserDetail.as_view())
]

# path('', views.ListRoles.as_view()),
# path('<int:pk>/', views.RoleDetail.as_view())