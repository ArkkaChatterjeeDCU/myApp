from django import forms
from .models import WeatherData


class WeatherDataForm(forms.ModelForm):
    HEAT_INDEX_CHOICES = [
        ('moderate', 'Moderate'),
        ('caution', 'Caution'),
        ('danger', 'Danger'),
    ]

    WIND_INDEX_CHOICES = [
        ('light_breeze', 'Light Breeze'),
        ('moderate_breeze', 'Moderate Breeze'),
        ('strong_winds', 'Strong Winds'),
        ('storm_force_winds', 'Storm Force Winds'),
    ]

    RAINFALL_INDEX_CHOICES = [
        ('light_occasional_rain', 'Light & Occasional Rain'),
        ('moderate_rain', 'Moderate Rain'),
        ('heavy_rain', 'Heavy Rain'),
        ('torrential_rain', 'Torrential Rain'),
    ]

    VISIBILITY_INDEX_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ]

    heat_index = forms.ChoiceField(choices=HEAT_INDEX_CHOICES)
    wind_index = forms.ChoiceField(choices=WIND_INDEX_CHOICES)
    rainfall_index = forms.ChoiceField(choices=RAINFALL_INDEX_CHOICES)
    visibility_index = forms.ChoiceField(choices=VISIBILITY_INDEX_CHOICES)
    location = forms.CharField(max_length=100, required=True)

    class Meta:
        model = WeatherData
        fields = ["heat_index", "wind_index", "rainfall_index", "visibility_index","location"]
        labels = {'heat_index': "heat_index", "wind_index": "wind_index", "rainfall_index":"rainfall_index",
                  "visibility_index":"visibility_index", "location":"location"}
