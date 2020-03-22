from django.shortcuts import render
from bs4 import BeautifulSoup
import requests, time, lxml
from selenium import webdriver

# Create your views here.
def cov_19(request):
    url = 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'
    browser = webdriver.PhantomJS("drivers/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    browser.get(url)
    time.sleep(10)
    page = browser.page_source
    soup = BeautifulSoup(page, 'lxml')

    context = {
        'totalConfirmed' : soup.find(id='ember26').find_all('g')[3].text,
        'deaths': soup.find(id='ember76').find_all('g')[3].text
    }
    return render(request, 'cov_19.html', context)
