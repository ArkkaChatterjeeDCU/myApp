#from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeatherData
from .forms import WeatherDataForm
from .utils import get_graph, get_gp2

def submit_weather(request):

    if request.method == "POST":
        usr =request.POST['user_id']
        heat_idx = request.POST['heat_index']
        wind_idx = request.POST['wind_index']
        rainfall_idx = request.POST['rainfall_index']
        visibility_idx= request.POST['visibility_index']
        loc = request.POST['location']
        wd = WeatherData(user=usr,heat_index= heat_idx, wind_index= wind_idx, rainfall_index=rainfall_idx,
                  visibility_index=visibility_idx, location=loc)
        wd.save()
        return redirect('view_weather')

    return render(request, 'submit_weather.html')


def view_weather(request):
    weather_data = WeatherData.objects.all()

    print("printing")
    print(weather_data)
    return render(request, 'view_weather.html', {'weather_data': weather_data})

def view_projection(request):

    pi_results = None
    pi_results_wind = None
    pi_results_rainfall = None
    pi_results_visibility = None

    if request.method == 'POST':

        selected_location = request.POST.get('location')
        if selected_location:
            filtered_data = WeatherData.objects.filter(location=selected_location)
            print(filtered_data)
            data = list(filtered_data.values())

            pi_results , pi_results_wind = get_graph(data)
            pi_results_rainfall, pi_results_visibility = get_gp2(data)
        else:
            filtered_data = None
    else:
        selected_location = ''
        filtered_data = None
    locations = WeatherData.objects.values_list("location",flat=True).distinct()

    context = {'unique_location':locations, 'pi': pi_results, 'pi_wind': pi_results_wind,
               'pi_rainfall': pi_results_rainfall, 'pi_visibility': pi_results_visibility}
    return render(request, 'data_projection.html', context)


