from django.db import models

# Create your models here.
from MyProject.api_basic.models import BaseModel
from MyProject.movies.Constants.ShowTimeValues import ShowTimeValues


class Movie(BaseModel):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MovieShowDetail(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    ticket_count = models.IntegerField()
    show_time = models.CharField(choices=ShowTimeValues.choices, max_length=100)
    show_date=models.DateField()

    def __str__(self):
        return self.movie.name +'-'+ str(self.show_time)


class MovieTicket(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_show_detail = models.ForeignKey(MovieShowDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + ' - ' + str(self.movie_show_detail.show_time)
