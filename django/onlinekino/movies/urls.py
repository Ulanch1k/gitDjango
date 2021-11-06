from django.urls import path
from .views import MovieView, MoviesDetailView,index_view, daily_kino, create_movie
from django.conf.urls import url
from django.views.generic import TemplateView

movie_urlpatterns = [
    path('api/movies/', MovieView.as_view()),
    path('api/movies/<int:pk>/', MoviesDetailView.as_view()),
    path('main/', index_view, name = 'main'),
    path('daily/', daily_kino, name = 'daily'),
    path('create/', create_movie, name = 'create')


]