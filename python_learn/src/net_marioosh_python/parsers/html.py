'''
Created on 2010-08-03

@author: marioosh
'''

from HTMLParser import HTMLParser
from urllib import urlopen

class SimplestParser (HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        req = urlopen(url)
        self.feed(req.read())

    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        print "Encountered the end of a %s tag" % tag

# p = SimplestParser('http://marioosh.net')
            
class MyParser (HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)   # super
        req = urlopen(url)
        self.data = req.read()
        self.startTag = None
        self.title = None
    
    def handle_starttag(self, tag, attrs):
        self.startTag = tag
        if tag == 'div' and attrs:
            for atr in attrs:
                atrName = atr[0]
                atrValue = atr[1]
        
    def handle_data(self, data):
        if(self.startTag == 'title'):
            self.title = str(self.title) + data
        #print('data: ' + data)
        
    def handle_endtag(self, tag):
        self.endTag = tag
        
    def unknown_decl(self, data):
        print ("UNKNOWN: "+data)

    def parse(self):
        self.feed(self.data)
                
    def getTitle(self):
        return self.title

p = MyParser('http://www.newtorrents.info/search/inception')
p.parse()
print ('TITLE:'+p.getTitle())

