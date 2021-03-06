from rest_framework import serializers
from rest_framework import generics
from .models import *
# This is a serializers
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

# this is a Model Serializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']

#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#
#
# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#
#
# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#
#
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#
#
# class BookingDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookingDetail
#
#
# class MovieTicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieTicket
#
#
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#
#
# class MovieShowDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieShowDetail
#
