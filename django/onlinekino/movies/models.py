from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True)
    rating = models.FloatField()
    release_date = models.DateField(auto_now=True)
    genres = models.CharField(max_length=40, default='Film')
