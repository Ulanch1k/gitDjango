from django.urls import path, include
from .views import MovieView, MoviesDetailView, index_view, daily_kino, create_movie, my_account, GenreView, GenreDetailView, IndexApi, admin_panel, login, YearFilterApi
from django.conf.urls import url
from django.views.generic import TemplateView

API_urlpatterns = [
    path('api/movies/', MovieView.as_view()),
    path('api/movies/<int:pk>/', MoviesDetailView.as_view()),
    path('api/genres/', GenreView.as_view()),
    path('api/genres/<int:pk>/', GenreDetailView.as_view()),
    path('api/count/', IndexApi.as_view()),
    path('api/year/', YearFilterApi.as_view()),
]

def_urlpatterns = API_urlpatterns +  [
    path('main/', index_view, name='main'),
    path('adminka/', admin_panel, name='adminka'),
    path('daily/', daily_kino, name='daily'),
    path('create/', create_movie, name='create'),
    path('account/', my_account, name='account'),
    path('login/', login, name='login'),
]