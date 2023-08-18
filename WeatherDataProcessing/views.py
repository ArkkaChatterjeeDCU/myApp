#from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeatherData
from .forms import WeatherDataForm
from .utils import get_graph


# @login_required
# def submit_weather(request):
#     if request.method == 'POST':
#         heat_index = request.POST['heat_index']
#         wind_index = request.POST['wind_index']
#         rainfall_index = request.POST['rainfall_index']
#         visibility_index= request.POST['visibility_index']
#         location = request.POST['location']
#         WeatherData.objects.create(
#             user=request.user,
#             heat_index=heat_index,
#             wind_index=wind_index,
#             rainfall_index=rainfall_index,
#             visibility_index=visibility_index,
#             location=location
#         )
#
#         return redirect('view_weather')
#     return render(request, 'WeatherDataProcessing/submit_weather.html')


def submit_weather(request):
    # if request.method == 'POST':
    #     form = WeatherDataForm(request.POST)
    #     if form.is_valid():
    #         print(form)
    # # Process the form data
    # # For example: Save the data to the database
    # # ...
    # else:
    #     form = WeatherDataForm()
    #
    # return render(request, 'submit_weather.html', {'form': form})

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

        #form = WeatherDataForm(request.POST)
    #     if form.is_valid():
    #         wdata = form.save(commit=False)
    #
    #         #wdata.save()
    # form = WeatherDataForm()
    return render(request, 'submit_weather.html')


def view_weather(request):
    weather_data = WeatherData.objects.all()

    print("printing")
    print(weather_data)
    return render(request, 'view_weather.html', {'weather_data': weather_data})

def view_projection(request):
    # weather_queryset = WeatherData.objects.all()
    # data = list(weather_queryset.values())
    # projection_json = get_location_json(data)

    if request.method == 'POST':
        pi_results = None
        selected_location = request.POST.get('location')
        if selected_location:
            filtered_data = WeatherData.objects.filter(location=selected_location)
            print(filtered_data)
            data = list(filtered_data.values())
            pi_results = get_graph(data)


        else:
            filtered_data = None
    else:
        selected_location = ''
        filtered_data = None
    locations = WeatherData.objects.values_list("location",flat=True).distinct()
    context = {'unique_location':locations, 'pi': pi_results}
    return render(request, 'data_projection.html', context)

    #return render(request,'data_projection.html')
