# -*- coding: utf-8 -*-
'''
Created on 2010-08-04

@author: marioosh
'''

from HTMLParser import HTMLParser
from urllib import urlopen

class SimplestParser (HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        req = urlopen(url)
        self.startTag = None
        self.duringLista = False
        self.i = 0
        
        self.feed(req.read())

    def handle_starttag(self, tag, attrs):
        self.startTag = tag
        
        if self.duringLista and tag == 'div' and attrs[0][1] == 'name':
            None
            
        if (tag == 'div' and attrs) or tag == 'div':
            for attr in attrs:
                attrName = attr[0]
                attrValue = attr[1]
                if attrName == 'class' and attrValue == 'lista':
                    print(self.getpos())
                    self.duringLista = True
                    break
        if tag == 'div' and self.duringLista:
            self.i += 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.duringLista:
            self.i -= 1
            if self.i == 0:
                self.duringLista = False
                print(self.getpos())
        
    def handle_data(self, data):
        if self.duringLista:
            print(data)
        
p = SimplestParser('http://www.eska.pl/goraca20')
