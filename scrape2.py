from bs4 import BeautifulSoup
import urllib2

f = open("./crimedata.csv", 'w')
error = open("./error.txt", 'w')

x = 0
while (x < 500)
    soup = BeautifulSoup (urllib2.urlopen('http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?uiTab=table').read() 'html')
    tableStats = soup.find('div', {'class' : '.ui-widget-content slick-row odd'})

    for
