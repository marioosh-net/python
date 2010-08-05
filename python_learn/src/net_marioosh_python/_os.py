'''
Created on 2010-07-29

@author: marioosh
'''

import os, sys

path = ''
# czy istnieje sciezka
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print '''
        syntax: ...
    '''
    
#print(path)
print(os.path.exists("/"))


if path == '':
    path = "."
print("path: "+path)

def info(path):
    # czy sciezka jest katalogiem ?
    if os.path.isdir(path):       
        # s = os.stat(f)
        print("DIR :"+path),
    else:
        print("FILE:"+path),
    # rozmiar pliku
    print(os.stat(path).st_size)


# lista plikow w katalogu
if os.path.isdir(path):
    list = os.listdir(path)                 
    for f in list:
        p = os.path.normpath(path+"/"+f)
        #info(os.path.join(path,f))
        info(p)
else:
    info(path)
    
