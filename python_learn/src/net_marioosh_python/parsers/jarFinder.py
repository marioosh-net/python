'''
Created on 2010-08-13

@author: marioosh
'''
# -*- coding: utf-8 -*-

# http://www.findjar.com/index.x?query=commons-beanutils-1.8.0.jar

import sys, os, argparse
from BeautifulSoup import BeautifulSoup
from urllib import urlopen

parser = argparse.ArgumentParser(os.path.basename(sys.argv[0]),description='find and download jar');
parser.add_argument('jar',help='jar name');
args = parser.parse_args(sys.argv[1:]);

url = urlopen('http://www.findjar.com/index.x?query='+args.jar)
soup = BeautifulSoup(url.read())
# print soup.prettify()
titleTag = soup.html.head.title
# print(str(titleTag))
print(str(titleTag.string))

# znajdz pierwszy pasujacy
lista = soup.find('table', attrs={'class': 'results'})
trs = lista.findAll('tr');
a = lista.find('tr').find('a');
print(a['href']);

# all tr
# for tr in trs:
#     a = tr.find('a');
#     print(a['href']);
