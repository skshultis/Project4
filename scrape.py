import requests
from lxml import etree
import urllib2
from bs4 import BeautifulSoup

url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?uiTab=table'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# response = requests.get(url, headers=headers)
# data = response.text
html = urllib2.urlopen(url).read()

#importing lxml was recommended to parse html rather than just soup = bs4.BeautifulSoup(html)
soup = BeautifulSoup(html, "lxml")
for data in soup.findAll('div', {'class': 'ui-widget-content slick-row odd'}):
    text = data.findChildren()[0].renderContents()
    print text

# info = soup.select('.slick-cell l6 r6')
#
# print info

# mydivs = soup.findAll('div')
# for div in mydivs:
#     if "class" in div:
#         if (div["class"]=="ui-widget-content slick-row odd"):
#             print div

#print table

#ui-widget-content slick-row odd
#attrs={'class': 'slick-cell l4 r4'}
# <div class="slick-cell l6 r6">5210 - 5299 BLOCK OF LOUGHBORO ROAD NW</div>

#this just gave a syntax error
# for div in soup.findAll('div', attrs={'class': 'ui-widget-content slick-row odd'})
#     print div.text
