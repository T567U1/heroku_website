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
    countries = ['canada', 'usa', 'uk', 'china']
    context = {
        'cases' : locale.format('%d', jsonFile['cases'], grouping=True),
        'deaths' : jsonFile['deaths'],
        'recovered' : jsonFile['recovered'],
        'data' : { country : get_country(country) for country in countries}
    }
    return render(request, 'cov_19.html', context)

def get_country(country):
    country_url = 'https://corona.lmao.ninja/v2/historical/' + country
    get_country = requests.get(country_url)
    jsonFile_ = get_country.json()
    day_ = jsonFile_['timeline']['cases']

    return day_
