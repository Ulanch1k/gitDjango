# Generated by Django 3.2.6 on 2021-10-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='realese_date',
            field=models.DateField(auto_now=True),
        ),
    ]