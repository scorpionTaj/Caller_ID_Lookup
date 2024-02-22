# Python
import requests
from bs4 import BeautifulSoup

def getdata(url):
    r=requests.get(url)
    return r.text

api = '63e6921030a7cf5ea08dd54da4201b2f'

# Ask the user for their number and country code
number = input("Please enter your number: ")
country = input("Please enter your country code: ")

htmldata = getdata('http://apilayer.net/api/validate?access_key=' + api + '&number=' + number + '&country_code=' + country + '&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)