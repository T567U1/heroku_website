from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import requests, time, lxml, os

# Create your views here.
def cov_19(request):
    chrome_options = webdriver.ChromeOptions()
    #production
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver = webdriver.Chrome(executable_path=r'C:/Webdrivers/chromedriver.exe')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
    time.sleep(15)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')

    context = {
        'totalConfirmed' : soup.find(id='ember26').find_all('g')[3].text,
        'deaths': soup.find(id='ember83').find_all('g')[3].text
    }
    driver.close()
    return render(request, 'cov_19.html', context)
