from django.urls import path
from .views import ListMovieShowDetail,ParticularMovieShowDetail


urlpatterns = [
    path('',ListMovieShowDetail.as_view()),
    path('<uuid:pk>/', ParticularMovieShowDetail.as_view())
]
