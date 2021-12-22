from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from MyProject.movies.models import Movie, MovieShowDetail
from MyProject.movies.serializers import MovieSerializer, MovieShowDetailSerializer
from MyProject.users.permissions import TicketBooking, ReadOnly,IsAdmin


class ListMovies(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [ReadOnly|IsAdmin]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [ReadOnly|IsAdmin]


class ListMovieShowDetail(generics.ListCreateAPIView):
    queryset = MovieShowDetail.objects.all()
    serializer_class = MovieShowDetailSerializer
    permission_classes = [ReadOnly|IsAdmin]


class ParticularMovieShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieShowDetail.objects.all()
    serializer_class = MovieShowDetailSerializer
    permission_classes = [ReadOnly|IsAdmin]