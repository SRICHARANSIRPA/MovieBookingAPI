from django.http import HttpResponse, JsonResponse
from rest_framework import mixins, generics,status

from MyProject.api_basic.serializers import *
from rest_framework.parsers import JSONParser
from .models import *

# Create your views here.
#
#
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)


class BaseView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    pass

#
# class UserView(BaseView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#
# def MovieView(request):
#     if request.method == 'GET':
#         queryset = Movie.objects.all()
#         serializer = MovieSerializer(queryset, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#         # return HttpResponse(serializer.data,status=status.HTTP_200_OK)
#
#
# def RoleView(request):
#     if request.method == 'GET':
#         queryset = Role.objects.all()
#         serializer = RoleSerializer(queryset, many=True)
#         return HttpResponse(serializer.data,status=status.HTTP_200_OK)
#

