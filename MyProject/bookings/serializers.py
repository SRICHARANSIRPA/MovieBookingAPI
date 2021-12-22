from rest_framework import serializers

from MyProject.bookings.Constants.Status import StatusValues
from MyProject.bookings.models import Booking, BookingDetail
from MyProject.movies.models import Movie, MovieShowDetail, MovieTicket
from MyProject.users.models import User


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetail
        fields = '__all__'


class MovieBookingSerializer(serializers.Serializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.filter(is_Active=True))
    showtime = serializers.PrimaryKeyRelatedField(queryset=MovieShowDetail.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    number_of_tickets = serializers.IntegerField()

    class Meta:
        fields = ['movie', 'showtime', 'number_of_tickets', 'user']

    def validate(self, attrs):
        attrs = super(MovieBookingSerializer, self).validate(attrs)
        number_of_tickets = attrs.get('number_of_tickets')
        movie = attrs.get('movie')
        movie_show_detail = attrs.get('showtime')
        user = attrs.get('user')
        if not movie_show_detail:
            raise serializers.ValidationError("No Movie Details found for movie -"+movie.name)
        if number_of_tickets > movie_show_detail.ticket_count:
            raise serializers.ValidationError('Ticket count is more')
        if movie_show_detail.movie.id != movie.id:
            raise serializers.ValidationError('Select valid movie Showtime for movie -'+movie.name)
        # print(user)
        # print(serializers.CurrentUserDefault())
        # if user != serializers.CurrentUserDefault():
        #     raise  serializers.ValidationError('select a valid user')
        return attrs

    def create(self, validated_data):
        movie = validated_data.get('movie')
        movie_show_detail = validated_data.get('showtime')
        number_of_tickets = validated_data.get('number_of_tickets')
        user = validated_data.get('user')
        print(validated_data)
        tickets = []
        for ticket_number in range(number_of_tickets):
            obj = MovieTicket(movie=movie, movie_show_detail=movie_show_detail)
            obj.save()
            tickets.append(obj)
        booking = Booking(status=StatusValues.BOOKED, user=user)
        booking.save()
        for ticket in tickets:
            booking_detail = BookingDetail(booking=booking, movie_Ticket=ticket)
            booking_detail.save()
        movie_show_detail.ticket_count = movie_show_detail.ticket_count - number_of_tickets
        movie_show_detail.save()
        return  dict(id = str(booking.id), movie_name=movie.name, showtime=movie_show_detail.show_time)

