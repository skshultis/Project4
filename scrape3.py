from bs4 import BeautifulSoup
import urllib2
import os
import urllib.request

f = open("./crimedata.csv", 'w')
error = open("./error.txt", 'w')

url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8?uiTab=table'
