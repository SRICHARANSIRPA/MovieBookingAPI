from django.db import models

# Create your models here.
from MyProject.api_basic.models import BaseModel
from MyProject.bookings.Constants.Status import StatusValues
from MyProject.users.models import User
from MyProject.movies.models import MovieTicket


class Booking(BaseModel):
    status = models.CharField(choices=StatusValues.choices, max_length=100)
    is_Active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking - ' + str(self.id)


class BookingDetail(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    movie_Ticket = models.ForeignKey(MovieTicket, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking - ' + str(self.booking.id) + ' - '+ self.movie_Ticket.movie.name + '('+str(self.booking.status)+')'
