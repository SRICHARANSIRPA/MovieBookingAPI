from django.contrib import admin

# Register your models here.
from MyProject.bookings.models import *

admin.site.register(Booking)
admin.site.register(BookingDetail)
