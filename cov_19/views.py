from django.http import JsonResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import requests, time, lxml, os, locale

# Create your views here.
def cov_19(request):
    base_url = "https://corona.lmao.ninja/all"
    response = requests.get(base_url)
    jsonFile = response.json()

    country_url = 'https://corona.lmao.ninja/v2/historical/canada'
    get_country = requests.get(country_url)
    jsonFile_ = get_country.json()
    day_ = jsonFile_['timeline']['cases']

    context = {
        'cases' : locale.format('%d', jsonFile['cases'], grouping=True),
        'deaths' : jsonFile['deaths'],
        'recovered' : jsonFile['recovered'],
        'data' : day_
    }
    return render(request, 'cov_19.html', context)
