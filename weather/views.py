from django.http import HttpResponse
from django.shortcuts import render
import requests
from .forms import WeatherForm



def home(request):
    api_key = 'b02fbb78b2c441438b342843232006'
    city = 'Arusha'
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'


    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data['Location']
        url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={selected}'
        response = requests.get(url)
        weather_data = response.json()
        temparature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        condition = weather_data['current']['condition']['text']
        town = weather_data['location']['name']
        region  = weather_data['location']['region']
        return render(request,"weather/base.html",{'town':town,'region':region,'temperature':temparature,'humidity':humidity,'condition':condition,'form':form})
    else:
        form = WeatherForm()
   
    response = requests.get(url)
    weather_data = response.json()
    temparature = weather_data['current']['temp_c']
    humidity = weather_data['current']['humidity']
    condition = weather_data['current']['condition']['text']
    town = weather_data['location']['name']
    region  = weather_data['location']['region']
    
    return render(request,"weather/base.html",{'town':town,'region':region,'temperature':temparature,'humidity':humidity,'condition':condition,'form':form})
    

# Create your views here.
