from django.db import models

# Create your models here.

from django.db import models
#from django.contrib.auth.models import User


class WeatherData(models.Model):
    # HEAT_INDEX_CHOICES = [
    #     ('moderate', 'Moderate'),
    #     ('caution', 'Caution'),
    #     ('danger', 'Danger'),
    # ]
    #
    # WIND_INDEX_CHOICES = [
    #     ('light_breeze', 'Light Breeze'),
    #     ('moderate_breeze', 'Moderate Breeze'),
    #     ('strong_winds', 'Strong Winds'),
    #     ('storm_force_winds', 'Storm Force Winds'),
    # ]
    #
    # RAINFALL_INDEX_CHOICES = [
    #     ('light_occasional_rain', 'Light & Occasional Rain'),
    #     ('moderate_rain', 'Moderate Rain'),
    #     ('heavy_rain', 'Heavy Rain'),
    #     ('torrential_rain', 'Torrential Rain'),
    # ]
    #
    # VISIBILITY_INDEX_CHOICES = [
    #    ('excellent', 'Excellent'),
    #    ('good', 'Good'),
    #    ('moderate', 'Moderate'),
    #    ('poor', 'Poor'),
    #    ('very poor', 'Very Poor')
    # ]

    user = models.CharField(max_length=100, default='')
    heat_index = models.CharField(max_length=100, default='')
    wind_index = models.CharField(max_length=100, default='')
    rainfall_index = models.CharField(max_length=100, default='')
    visibility_index = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.location}'

