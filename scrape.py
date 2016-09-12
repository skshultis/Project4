import requests
import lxml.etree
from bs4 import BeautifulSoup

url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?uiTab=table'
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "lxml")
table = soup.find_all('div', attrs={'class': 'ui-widget-content slick-row odd'})

print table
