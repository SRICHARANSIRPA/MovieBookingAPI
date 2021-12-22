from django.urls import path
from .views import ListMovies,MovieDetail


urlpatterns = [
    path('',ListMovies.as_view()),
    path('<uuid:pk>/', MovieDetail.as_view())
]
