import csv
import requests
from bs4 import BeautifulSoup

#url for DC OpenData crime incidents in the last 30 days
url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?uiTab=table'
response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html)
table = soup.find('div', attrs={'class': 'slick-viewport'})

list_of_rows = []
for row in table.findAll()

print html

type = soup.find('div',attrs={"class":"table-info"}).findAll('div')
print type[2].find('strong').string
# {'class': 'recline-slickgrid slickgrid_286674 ui-widget' , 'id': 'attribute-table'}
