'''
Created on 2011-01-27

@author: marioosh
'''
# -*- coding: utf-8 -*-

import argparse # parser argumentow wejsciowych
import os, sys
import zipfile

# parsowanie argumentow
parser = argparse.ArgumentParser(description='Zipper')
parser.add_argument('-c',help='destination directory',default='DEST',type=string,metavar='value')
parser.add_argument('file1',help='source directory')
parser.add_argument('file2',help='destination directory')
parser.print_help()
args = parser.parse_args(sys.argv[1:])
f1 = args.file1
f2 = args.file2

os.mkdir()