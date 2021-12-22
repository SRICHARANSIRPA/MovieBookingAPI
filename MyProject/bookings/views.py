from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from MyProject.users.models import User
from MyProject.bookings.models import *
# Create your views here.
from MyProject.bookings.serializers import BookingSerializer, BookingDetailSerializer, MovieBookingSerializer
from MyProject.users.models import UserRole
from MyProject.users.permissions import TicketBooking, ReadOnly, IsAdmin
from MyProject.bookings.models import Booking,BookingDetail
from MyProject.users.models import User


class ListBookings(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdmin]


class ListBooking(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ListBookingDetails(generics.ListCreateAPIView):
    queryset = BookingDetail.objects.all()
    serializer_class = BookingDetailSerializer
    permission_classes = [TicketBooking]


class ListBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingDetail.objects.all()
    serializer_class = BookingDetailSerializer


class MovieBooking(generics.ListCreateAPIView):
    serializer_class = MovieBookingSerializer
    queryset = Booking.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user or request.user.is_anonymous:
            return Response('No User', status=401)
        bookings=Booking.objects.filter(user=request.user)
        serializer=BookingSerializer(bookings, many=True)
        return Response(data=serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        if not request.user or request.user.is_anonymous:
            return Response('No User', status=401)
        user_role = UserRole.objects.filter(user=request.user, is_current=True).first()
        if not user_role:
            return Response('No User', status=401)
        if not user_role.role.can_book_ticket:
            return Response('No User', status=401)
        # user_id = User.objects.filter(request.user).first()
        # data = json.loads(request.data)
        # data['user'] = user_id.id

        serializer = MovieBookingSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.save(), status=201)
        return Response(serializer.errors, status=400)


