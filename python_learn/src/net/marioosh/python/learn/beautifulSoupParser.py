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
# print(str(titleTag))
print(str(titleTag.string))

# znajdz pierwszy pasujacy
lista = soup.find('div', attrs={'class': 'lista'})
# znajdz wszystkie
l = lista.findAll('div', attrs={'class': 'name'})
for e in l:
    
    # artist
    spanFirst = e.find('span', attrs={'class': 'first'});
    x = spanFirst.findAll('a')
    j = 0
    for i in x:
        j += 1
        print(i.string.strip()),
        if len(x) > 1 and j < len(x):
            print(','),
    # title
    print(" - " + spanFirst.findNextSibling('span').find('a').string.strip())
