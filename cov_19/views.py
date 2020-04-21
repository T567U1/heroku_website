from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import requests, time, lxml, os, locale

# Create your views here.
def cov_19(request):
    base_url = "https://corona.lmao.ninja/v2/all"
    response = requests.get(base_url)
    jsonFile = response.json()
    countries = ['canada', 'usa', 'uk', 'spain', 'netherlands', 'italy', 'colombia']
    context = {
        'cases' : '{:,}'.format(jsonFile['cases']),
        'active' : '{:,}'.format(jsonFile['cases'] - jsonFile['deaths'] - jsonFile['recovered']),
        'deaths' : '{:,}'.format(jsonFile['deaths']),
        'recovered' : '{:,}'.format(jsonFile['recovered']),
        'data' : { country : get_country(country) for country in countries},
        'grow_over_time' : { 'cases' : get_grow_over_time('cases'), 'deaths' : get_grow_over_time('deaths')},
        'get_country_total' : get_country_total()
    }
    return render(request, 'cov_19.html', context)

def get_country(country):
    country_url = 'https://corona.lmao.ninja/v2/historical/' + country
    get_country = requests.get(country_url)
    jsonFile_ = get_country.json()
    get_data = list(jsonFile_['timeline']['cases'])
    day_ = {}
    i = 0
    for x in jsonFile_['timeline']['cases']:
        if i == 0:
            day_[x] = jsonFile_['timeline']['cases'][x]
        i += 1 if i < 7 else -7
    day_[get_data[-1]] = jsonFile_['timeline']['cases'][get_data[-1]]

    return day_

def get_grow_over_time(str):
    grow_over_time_url = 'https://corona.lmao.ninja/v2/historical/all'
    get_grow = requests.get(grow_over_time_url)
    jsonFile_ = get_grow.json()
    get_data = jsonFile_[str]

    return get_data

def get_country_total():
    get_info = requests.get('https://corona.lmao.ninja/v2/countries')
    jsonFile_ = get_info.json()

    return jsonFile_
