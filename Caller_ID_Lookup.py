# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data
# Making a GET request
	
def getdata(url):
	r=requests.get(url)
	return r.text
# API key
# Enter your own API key instead of 'YOUR API KEY'
api = '63e6921030a7cf5ea08dd54da4201b2f'

# number and country code
number = '627749814'
country = 'MA'

# pass Your API, number and country code
# in getdata function
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)
