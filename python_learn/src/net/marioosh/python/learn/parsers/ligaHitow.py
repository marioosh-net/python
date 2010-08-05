'''
Created on 2010-08-04

@author: marioosh
'''

from BeautifulSoup import BeautifulSoup
from urllib import urlopen

url = urlopen('http://www.radiozet.pl/liga-hitow/')
soup = BeautifulSoup(url.read())
titleTag = soup.html.head.title
print(str(titleTag.string).strip() + '<br/><br/>')

notowanie = soup.find('div', attrs={'class': 'notowanie'})
voteable = notowanie.find('div', attrs={'class':'voteable'})
for dl in voteable.findAll('dl'):
    artist = dl.find('dd', attrs={'class':'artist'})
    print('<span style="font-weight: bold;">' + str(artist.next.string).strip() + '</span> - '),
    track = dl.find('dd', attrs={'class':'track'})
    print(str(track.string).strip() + '<br/>')