#!/usr/bin/python
# -*- coding: utf-8 -*-
import mimetypes, os, argparse, sys

def visit(arg, dirName, fileNames):
    for f in fileNames:
        fullPath = os.path.normpath(os.path.join(dirName,f))
        if not os.path.isdir(fullPath):
            ext = str(os.path.splitext(fullPath)[1]).lower()
            if ext in [args.ext.lower()]:
                print(fullPath)
                #fo.write(os.path.relpath(fullPath,args.path)+'\n')
                if args.p == False:
                    fo.write(fullPath+'\n')
                    os.remove(fullPath)

parser = argparse.ArgumentParser('extRemover',description='Remove files with some extension from path');
parser.add_argument('path',help='path from files will be removed');
parser.add_argument('ext',help='file extension to remove');
parser.add_argument('logfile',nargs='?',default='extRemover.log',help='log file');
parser.add_argument('-p',help='show files, DON\'T DELETE',action='store_true');
args = parser.parse_args(sys.argv[1:]);

if args.p == False:
    fo = open(args.logfile,'w')
os.path.walk(args.path, visit, 1)
if args.p == False:
    fo.close()


