This is where I put extra stuff, like blocks of code that I might want to refer back to, or things I find that will be applicable later.

replacing two strings at once
'obama'.replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b')
'oabmb'

************
restarting scraper

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

*****************************
thinking about D3:
<script src="https://d3js.org/d3.v4.min.js"></script>
