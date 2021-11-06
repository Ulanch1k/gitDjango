from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    def validate(self, attr):
        if attr['rating'] <= 0 or attr['rating'] > 10:
            raise ValidationError('Недопустимое значение')
        return attr

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "rating", "genre", "release_date")


class MovieDetailSerializer(serializers.ModelSerializer):

    def validate(self, attr):
        if attr['rating'] <= 0 or attr['rating'] > 10:
            raise ValidationError('Недопустимое значение')
        return attr

    class Meta:
        model = Movie
        fields = ('__all__')

