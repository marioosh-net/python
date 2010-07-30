'''
Created on 2010-07-30

@author: marioosh
'''

import os, sys, mimetypes

class Message:
    # wyswietlanie komunikatow
    @staticmethod
    def debug(m):
        print("DEBUG: " + m)
    @staticmethod
    def info(m):
        print("INFO: " + m)
    @staticmethod
    def error(m):
        print("ERROR: " + m)
        
class Params:
    # pobieranie parametrow
    def __init__(self, minParams, errorMessage):
        self.minParams = minParams
        if len(sys.argv) <= self.minParams:
            print(errorMessage)
            exit()
        self.params = sys.argv[1:]
             
class AlbumMaker:
    # resize obrazkow
    def __init__(self, sourcePath, destPath):
        self.sourcePath = sourcePath
        self.destPath = destPath
        if os.path.exists(s) and os.path.exists(d):
            Message.info("paths ok")
        else:
            Message.error("paths not ok")
            exit()
        self.doit()
        
    def doit(self):
        print ('---------- START ----------')
        print ("source     : " + self.sourcePath)
        print ("destination: " + self.destPath)
        
        # dla kazdego katalogu wywolaj metode visit
        os.path.walk(self.sourcePath, self.__visit, 1)
    
    def __visit(self, arg, dirName, fileNames):
        for f in fileNames:
            fullPath = os.path.normpath(os.path.join(dirName,f))
            if not os.path.isdir(fullPath):
                mime = mimetypes.guess_type(fullPath)[0]
                if mime in ['image/jpeg', 'image/gif', 'image/pjpeg']:
                    print(fullPath)

p = Params(1, '''
    syntax: album_maker [<source path>] <destination path>
    ''')
s = p.params[0]
if len(p.params) < 2:
    s = '.'
    d = p.params[0]
else:
    d = p.params[1]
    
a = AlbumMaker(s,d)

    