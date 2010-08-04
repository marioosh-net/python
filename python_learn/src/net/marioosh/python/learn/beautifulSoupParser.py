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
    #spanFirst = e.find('span', attrs={'class': 'first'});
    #print(spanFirst),
    a = e.findAll('a');
    print(a[0].string.lstrip() + " : "),
    print(a[1].string.lstrip())
#    for k in a:
#        print(k.string),
#    print ''
    # print(e.findAll('a'))
    #print(e.find('span', attrs={'class': 'first'}).string), 
    #print(e.find('a').string)

# soup2 = BeautifulSoup(str(lista))
# print str(soup2.prettify())

