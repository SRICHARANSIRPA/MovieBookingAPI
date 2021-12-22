"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/Movies/', include('MyProject.movies.urls')),
    path('api/MovieShowDetails/', include('MyProject.movies.movie_show_detail_urls')),
    path('api/Users/', include('MyProject.users.urls')),
    path('api/Roles/',include('MyProject.users.Role_urls')),
    path('api/UserRoles/',include('MyProject.users.User_role_urls')),
    path('api/Bookings/',include('MyProject.bookings.urls')),
    path('api/BookingDetails/',include('MyProject.bookings.booking_detail_urls')),
    path('api/MovieBooking/',include('MyProject.bookings.movie_booking_urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

