from django.urls import path
from .views import MovieView, MoviesDetailView,IndexView
from django.conf.urls import url
from django.views.generic import TemplateView

movie_urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:pk>/', MoviesDetailView.as_view()),

]