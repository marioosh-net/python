'''
Created on 2010-08-03

@author: marioosh
'''
from HTMLParser import HTMLParser
from urllib import urlopen

class MyParser (HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)   # super
        self.startTag = None
        self.title = ''
        req = urlopen(url)
        try:        
            self.feed(req.read())
        except:
            None
    
    def handle_starttag(self, tag, attrs):
        self.startTag = tag
        
    def handle_data(self, data):
        if(self.startTag == 'title'):
            self.title += data
        
    def handle_endtag(self, tag):
        self.endTag = tag
        
    def getTitle(self):
        return self.title

p = MyParser('http://swistak.pl')
print(p.getTitle())
