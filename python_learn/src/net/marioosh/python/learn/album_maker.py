'''
Created on 2010-07-30

@author: marioosh
'''

import os, sys, mimetypes
from utils import Message, Params

class AlbumMaker:
    # resize obrazkow
    def __init__(self, sourcePath, destPath):
        self.sourcePath = sourcePath
        self.destPath = destPath
        if os.path.exists(s):
            Message.info("source path ok")
        else:
            Message.error("source path doesn't exist")
            exit()
        if os.path.exists(d):
            if os.path.isdir(d):
                if os.listdir(d) == []:
                    Message.info("destination path ok")
                else:
                    Message.error("destination directory not empty")
                    exit()                    
            else:
                Message.error("destination path is file")
                exit()
        else:
            try:
                # stworz katalog docelowy
                os.makedirs(d, mode=0755)
            except:
                print("can't make destination directory")
                exit()

        self.doit()
        
    def doit(self):
        print ('---------- START ----------')
        print ("source     : " + self.sourcePath)
        print ("destination: " + self.destPath)
        
        # dla kazdego katalogu wywolaj metode visit
        os.path.walk(self.sourcePath, self.__process, 1)
    
    def __process(self, arg, dirName, fileNames):
        # przetworz jeden katalog
        for f in fileNames:
            fullSourcePath = os.path.normpath(os.path.join(dirName,f))
            if not os.path.isdir(fullSourcePath):
                mime = mimetypes.guess_type(fullSourcePath)[0]
                if mime in ['image/jpeg', 'image/gif', 'image/pjpeg']:
                    print(fullSourcePath),
                    fullDestPath = os.path.join(self.destPath, os.path.relpath(fullSourcePath, self.sourcePath))
                    print(fullDestPath)

p = Params(1, 'syntax: album_maker [<source path>] <destination path>')
s = p.params[0]
if len(p.params) < 2: 
    s = '.' 
    d = p.params[0]
else: d = p.params[1]
    
a = AlbumMaker(s,d)
