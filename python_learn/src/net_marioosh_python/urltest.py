'''
Created on 2010-07-28

@author: marioosh
'''
from utils import p
import urllib

# downloading file
urllib.urlretrieve("http://old.marioosh.net/test.txt","test2.txt")

# otwarcie zasobu sieciowego do odczytu
f = urllib.urlopen("http://onet.pl/")
end = False
w = open('out.html','w')
while not end:
    x = f.read(1)
    if(x != ''):
        # wywalam taby i entery
        if x not in set(['\t', '\n']):
            p(x)
            w.write(x)
    else:
        end = True
        
