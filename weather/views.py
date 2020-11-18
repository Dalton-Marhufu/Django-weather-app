from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

#Home page Function
def index(request):
    url =  'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=46a3b3ce2a940322a6965e7e6e433cc1'
    err_message = ""


    # POST method to API
    if request.method == 'POST':
        form = CityForm(request.POST)

        #Form vslidation
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist in the world!'

            else:
                err_msg = "City already exists in the database"


    #form
    form = CityForm()

    #Data base query to return all cities
    cities = City.objects.order_by('-date_posted')

    #Creating a dictionary list
    weather_data = []

    #Loop through the database
    for city in cities:

        #URL responce converted to json object
        r = requests.get(url.format(city)).json()

        #Dictionary list to extract data from API
        city_weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'temperature_min' : r['main']['temp_min'],
            'temperature_max' : r['main']['temp_max'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            }


        #Adding new city to the list
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data,'form':form}
    return render(request, 'weather/weather.html', context)


#Delete function to be added
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')
