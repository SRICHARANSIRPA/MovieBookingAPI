from rest_framework import serializers

from MyProject.movies.models import Movie, MovieShowDetail


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'is_Active']


class MovieShowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShowDetail
        fields = ['id', 'movie', 'ticket_count', 'show_time', 'show_date']
