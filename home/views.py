from django.shortcuts import render
from ipware import get_client_ip

# Create your views here.
def get_ip(request):
    ip = {'ip': get_client_ip(request)}

    return render(request, 'home.html', ip)
