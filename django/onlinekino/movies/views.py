from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from django.views.generic import TemplateView
from django.db.models import Count



from .serializers import MovieSerializer, MovieDetailSerializer
from .models import Movie

# Create your views here.

class MovieView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny, )

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)

class MoviesDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        return super().retrieve(request, pk)

    def delete(self, request, pk):
        return super().destroy(request, pk)

    def put(self, request, pk):
        return super().update(request, pk)

    def patch(self, request, pk):
        return super().partial_update(request, pk)


def IndexView(request):
    data = Movie.objects.aggregate(count=Count('id'))
    print(data)
    return render(request, 'index.html', {'data': data})


def DailyKino(request):
    return render(request, "daykino.html")

def createMovie(request):
    return render(request, "create_film.html")
