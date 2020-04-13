from django.shortcuts import render
from ipware import get_client_ip
import requests

# Create your views here.
def get_ip(request):
    ip = get_client_ip(request)
    try:
        ip_info = requests.get(f'https://geo.ipify.org/api/v1?apiKey=at_FIfs0SjKrCBmADYEqiGrHYDakY1FP&ipAddress={ip[0]}')
    except:
        ip_info = requests.get(f'https://geo.ipify.org/api/v1?apiKey=at_FIfs0SjKrCBmADYEqiGrHYDakY1FP&ipAddress=8.8.8.8')
    ip_json = ip_info.json()

    get_ip_info = {
        'ip': ip_json['location']['country'],
        'test': 'hello',
    }

    return render(request, 'home.html', get_ip_info)
