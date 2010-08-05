'''
Created on 2010-08-04

@author: marioosh
'''

from BeautifulSoup import BeautifulSoup
from urllib import urlopen

req = urlopen('http://www.rmf.fm/au/?a=poplista')
soup = BeautifulSoup(req.read())
# print soup.prettify()
titleTag = soup.html.head.title
# print(str(titleTag))
print(str(titleTag.string))

# znajdz pierwszy pasujacy
lista = soup.find('td', attrs={'width': '690'})
# znajdz wszystkie
l1 = lista.find('table', attrs={'class': 'poplista-toptable'})
print (l1);
print ('---------------');
l2 = l1.findNextSibling('table')
print(l2);
    

