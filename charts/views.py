from django.shortcuts import render
from .forms import CityCharts
import requests
from django.http import JsonResponse

# same entry Form for reqest
def charts(request):

    return render(request, 'charts/charts.html')

def chartdata(request):
    url =  'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=46a3b3ce2a940322a6965e7e6e433cc1'
    data = 'benoni'
    r = requests.get(url.format(data))

    graph_data = {

        'city' : r['name'],
        'temperature_min' : r['main']['temp_min'],
        'temperature_max' : r['main']['temp_max'],
    }

    return JsonResponse (graph_data, safe=false)
