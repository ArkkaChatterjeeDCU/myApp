from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_weather, name='home'),  # Add this line for the root path
    path('submit-WeatherDataProcessing/', views.submit_weather, name='submit_weather'),
    path('view-WeatherDataProcessing/', views.view_weather, name='view_weather'),
    path('view-WeatherDataProjection/', views.view_projection, name='data_projection')
    #path(r'form', views.submit_weather, name='form')
]
