'''
Created on 2010-08-04

@author: marioosh
'''

from BeautifulSoup import BeautifulSoup
from urllib import urlopen

req = urlopen('http://www.eska.pl/goraca20')
soup = BeautifulSoup(req.read())
# print soup.prettify()
titleTag = soup.html.head.title
print(titleTag)
print(titleTag.string)

soup2 = BeautifulSoup(str(soup.findAll('div', attrs={'class': 'lista'})))
print soup2.prettify()

