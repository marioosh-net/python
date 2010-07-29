'''
Created on 2010-07-29

@author: marioosh
'''

import os, sys

# czy istnieje sciezka
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print '''
        syntax: ...
    '''
    exit()
#print(path)
print(os.path.exists("/"))
