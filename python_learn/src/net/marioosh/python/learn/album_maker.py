#!/usr/bin/python

'''
Created on 2010-07-30

@author: marioosh
'''

import os, sys, mimetypes
from shutil import copyfile
import argparse # parser argumentow wejsciowych
import subprocess 

def debug(m):
    print("DEBUG: " + m)
def info(m):
    print("INFO: " + m)
def error(m):
    print("ERROR: " + m)
    
class AlbumMaker:
    # resize obrazkow
    def __init__(self, sourcePath, destPath):
        self.sourcePath = sourcePath
        self.destPath = destPath
        self.doit()
        
    def doit(self):
        print ('---------- START ------------------------------------')
        print ("source       : " + self.sourcePath)
        print ("destination  : " + self.destPath)
        print ("quality      : " + str(quality))
        print ("width/height : " + str(wh))
        print ("with subdirs : " + str(processSubdirs))
        print ('-----------------------------------------------------')
        self.resized = 0
        self.copied = 0
       
        if processSubdirs:
            # dla kazdego katalogu wywolaj metode visit
            os.path.walk(self.sourcePath, self.__process, 1)
        else:
            self.__process(1, self.sourcePath, os.listdir(self.sourcePath))
        
        print ('Processed: ' + str(self.resized+self.copied) + ' ('+'copied: ' + str(self.copied)+', resized: ' + str(self.resized) + ')')
    
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
                        convert = 'convert -quality '+str(quality)+' -resize '+str(wh)+'x'+str(wh)+' "' + fullSourcePath + '" "' + fullDestPath + '"'
                        subprocess.call(convert, shell=True)
                        print('DONE (resized)'.ljust(20))
                        self.resized += 1
                    else:
                        # kopiuj plik
                        copyfile(fullSourcePath, fullDestPath)
                        print('DONE (copied)'.ljust(20))
                        self.copied += 1

# parsowanie argumentow
parser = argparse.ArgumentParser(description='Make WEB-ready (smaller) photos')
parser.add_argument('-o',help='overwrite destination directory',action='store_true')
parser.add_argument('-c',help='create destination directory if not exist',action='store_true')
parser.add_argument('-s',help='max file size (larger will be resized)',default=200000,type=int,metavar='filesize')
parser.add_argument('-wh',help='width (and height) destination image',default=800,type=int,metavar='pixels')
parser.add_argument('-q',help='quality of destination image',default=80,type=int,metavar='value')
parser.add_argument('source',help='source directory')
parser.add_argument('-r',help='read all files under each directory, recursively',action='store_true')
parser.add_argument('destination',help='destination directory')
#parser.print_help()
args = parser.parse_args(sys.argv[1:])
c_opt = args.c
o_opt = args.o
s = args.source
d = args.destination
wh = args.wh
maxFileSize = args.s
quality = args.q
processSubdirs = args.r 

# sprawdzanie poprawnosci podanych argumentow
if not os.path.exists(s):
    error("source path doesn't exist")
    exit()
    
if os.path.exists(d):
    if os.path.isdir(d):
        if os.listdir(d) == []:
            info("destination path ok")
        else:
            if not o_opt:
                error("destination directory not empty")
                exit()
    else:
        error("destination path is file")
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
        error("destination directory doesn't exist")
        exit()


# wywolanie makera :D
a = AlbumMaker(s,d)
