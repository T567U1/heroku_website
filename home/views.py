from django.shortcuts import render
from ipware import get_client_ip
import requests

# Create your views here.
def get_ip(request):
    ip = get_client_ip(request)
    if ip[1]:
        weather = get_ip_info(ip[0])
        weather['ip'] = ip[0]
        weather['access'] = ip[1]

    else:
        weather = {'ip': ip[1]}

    return render(request, 'home.html', weather)

def get_ip_info(ip):
    api_key = 'at_FIfs0SjKrCBmADYEqiGrHYDakY1FP'
    ip_info = requests.get(f'https://geo.ipify.org/api/v1?apiKey={api_key}&ipAddress={ip}')
    ip_json = ip_info.json()

    return get_weather(ip_json['location']['country'], ip_json['location']['city'])

def get_weather(country_code, city):

    api_key = "2f98ded56c73b2ff50dd947e6df2b329"
    city = city.split()[0]
    base_url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country_code.lower()}")
    weather_json = base_url.json()

    rsp = {
        'country': country_code,
        'city': city,
        'temp': weather_json['main']['temp'] - 273.15
    }

    return rsp
