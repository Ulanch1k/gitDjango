from django.urls import path
from .views import MovieView, MoviesDetailView,IndexView, DailyKino, createMovie
from django.conf.urls import url
from django.views.generic import TemplateView

movie_urlpatterns = [
    path('api/movies/', MovieView.as_view()),
    path('api/movies/<int:pk>/', MoviesDetailView.as_view()),
    path('main/', IndexView, name = 'main'),
    path('daily/', DailyKino, name = 'daily'),
    path('create/', createMovie, name = 'create')


]