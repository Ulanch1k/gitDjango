from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a movie genre")

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True)
    rating = models.FloatField()
    release_date = models.DateField(auto_now=True)
    genre = models.ManyToManyField(Genre, default='Фильм')
