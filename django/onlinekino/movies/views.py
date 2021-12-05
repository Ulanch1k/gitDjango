from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from django.db.models import Count



from .serializers import MovieSerializer, MovieDetailSerializer, GenreSerializer
from .models import Movie, Genre

# Create your views here.


class GenreView(GenericAPIView, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny, )

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class GenreDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        return super().retrieve(request, pk)

    def delete(self, request, pk):
        return super().destroy(request, pk)

    def put(self, request, pk):
        return super().update(request, pk)

    def patch(self, request, pk):
        return super().partial_update(request, pk)


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


class IndexApi(APIView):
    def get(self, request):
        movie_count = Movie.objects.count()
        context = {"count": movie_count}
        print(movie_count)
        return Response(status=200, data=context)


def index_view(request):
    return render(request, 'index.html')

def admin_panel(request):
    return render(request, 'admin-panel.html')

def daily_kino(request):
    return render(request, "daykino.html")

def create_movie(request):
    return render(request, "create_film.html")

def my_account(request):
    return render(request, "MyAccount.html")

