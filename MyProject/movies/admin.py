from django.contrib import admin

# Register your models here.
from MyProject.movies.models import *

admin.site.register(Movie)
admin.site.register(MovieShowDetail)
admin.site.register(MovieTicket)