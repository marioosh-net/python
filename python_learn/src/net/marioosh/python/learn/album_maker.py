#!/usr/bin/python

'''
Created on 2010-07-30

@author: marioosh
'''

import os, sys, mimetypes
from utils import Message, Params
from shutil import copyfile
import argparse # parser argumentow wejsciowych
import subprocess 

class AlbumMaker:
    # resize obrazkow
    def __init__(self, sourcePath, destPath):
        self.sourcePath = sourcePath
        self.destPath = destPath
        self.doit()
        
    def doit(self):
        print ('---------- START ------------------------------------')
        print ("source     : " + self.sourcePath)
        print ("destination: " + self.destPath)
        print ('-----------------------------------------------------')
       
        # dla kazdego katalogu wywolaj metode visit
        os.path.walk(self.sourcePath, self.__process, 1)
    
    def __process(self, arg, dirName, fileNames):
        # przetworz jeden katalog
        for f in fileNames:
            fullSourcePath = os.path.normpath(os.path.join(dirName,f))
            # fd = os.path.splitext(f)[0] + '_large' + os.path.splitext(f)[1]
            if not os.path.isdir(fullSourcePath):
                mime = mimetypes.guess_type(fullSourcePath)[0]
                if mime in ['image/jpeg', 'image/pjpeg']:
                    
                    fileSize = os.path.getsize(fullSourcePath)
                    #print(fullSourcePath),
                    fullDestPath = os.path.join(self.destPath, os.path.relpath(fullSourcePath, self.sourcePath))
                    x = os.path.splitext(fullDestPath)
                    fullDestPath = x[0] + '_large' + x[-1]
                    
                    # stworz katalog docelowy jesli nie istnieje
                    dird = os.path.dirname(fullDestPath)
                    if not os.path.exists(dird):
                        os.makedirs(dird, mode=0755)

                    #ps='Processing "' + f + '" ... '
                    ps='Processing "' + fullSourcePath + '" ... '
                    print(ps.ljust(100)),                    
                    if fileSize > int(maxFileSize):
                        # resize
                        convert = 'convert -quality 80 -resize '+str(wh)+'x'+str(wh)+' "' + fullSourcePath + '" "' + fullDestPath + '"'
                        subprocess.call(convert, shell=True)
                        print('DONE (resized)'.ljust(20))
                    else:
                        # kopiuj plik
                        copyfile(fullSourcePath, fullDestPath)
                        print('DONE (copied)'.ljust(20))

# parsowanie argumentow
parser = argparse.ArgumentParser(description='Make WEB-ready (smaller) photos')
parser.add_argument('-o',help='overwrite destination directory',action='store_true')
parser.add_argument('-c',help='create destination directory if not exist',action='store_true')
parser.add_argument('-s',help='max file size (larger will be resized)',default=200000,type=int,metavar='filesize')
parser.add_argument('-wh',help='width (and height) destination image',default=800,type=int,metavar='pixels')
parser.add_argument('source',help='source directory')
parser.add_argument('destination',help='destination directory')
#parser.print_help()
args = parser.parse_args(sys.argv[1:])
c_opt = args.c
o_opt = args.o
s = args.source
d = args.destination
wh = args.wh
maxFileSize = args.s

# sprawdzanie poprawnosci podanych argumentow
if not os.path.exists(s):
    Message.error("source path doesn't exist")
    exit()
    
if os.path.exists(d):
    if os.path.isdir(d):
        if os.listdir(d) == []:
            Message.info("destination path ok")
        else:
            if not o_opt:
                Message.error("destination directory not empty")
                exit()
    else:
        Message.error("destination path is file")
        exit()
else:
    if c_opt:
        try:
            # stworz katalog docelowy
            os.makedirs(d, mode=0755)
        except:
            print("can't make destination directory")
            exit()
    else:
        Message.error("destination directory doesn't exist")
        exit()


# wywolanie makera :D
a = AlbumMaker(s,d)
