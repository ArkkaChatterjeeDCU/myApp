from django.db import models

# Create your models here.

from django.db import models
#from django.contrib.auth.models import User


class WeatherData(models.Model):


    user = models.CharField(max_length=100, default='')
    heat_index = models.CharField(max_length=100, default='')
    wind_index = models.CharField(max_length=100, default='')
    rainfall_index = models.CharField(max_length=100, default='')
    visibility_index = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.location}'

