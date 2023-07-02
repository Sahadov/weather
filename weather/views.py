import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    appid = '79692111fc51490e8ba21318230805'
    url = 'http://api.weatherapi.com/v1/current.json?key=' + appid + '&q={}&aqi=no'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    

    cities = City.objects.all()
    all_cities = []

    for city in cities:

        res = requests.get(url.format(city)).json()

        city_info = {
            'city': city.name,
            'country': res['location']['country'],
            'time': res['location']['localtime'],
            'temp': res['current']['temp_c'],
            'icon': res['current']['condition']['icon']
        }    

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    
    return render(request, 'weather/index.html', context)

def history(request):
    return render(request, 'weather/history.html', {})