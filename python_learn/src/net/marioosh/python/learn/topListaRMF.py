'''
Created on 2010-08-04

@author: marioosh
'''

from BeautifulSoup import BeautifulSoup
from urllib import urlopen

req = urlopen('http://www.rmf.fm/au/?a=poplista')
soup = BeautifulSoup(req.read())
titleTag = soup.html.head.title
print(str(titleTag.string) + '<br/><br/>')

lista = soup.find('td', attrs={'width': '690'})

# top 3
l1 = lista.find('table', attrs={'class': 'poplista-toptable'})
for tr in l1.findAll('tr'):
    print(str('<span style="font-weight: bold;">' + tr.contents[2].next.string.strip() + '</span> - ')),
    print(str(tr.contents[2].next.nextSibling.nextSibling.string.strip() + '<br/>'))

# reszta
l2 = l1.findNextSibling('table')
for tr in l2.contents:
    drugiTd = tr.contents[1];
    print(str('<span style="font-weight: bold;">' + drugiTd.next.string.strip() + '</span>')),
    print(str(drugiTd.next.nextSibling.string.strip() + '<br/>'))

    

