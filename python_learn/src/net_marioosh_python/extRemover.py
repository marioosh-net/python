# -*- coding: utf-8 -*-
import mimetypes, os, argparse, sys
parser = argparse.ArgumentParser('extRemover',description='Remove files with some extension from path');
parser.add_argument('path',help='path from files will be removed and logged to file');
parser.add_argument('ext',help='file extension to remove');
parser.add_argument('logfile',nargs='?',default='extRemover.log',help='log file');
args = parser.parse_args(sys.argv[1:]);

def visit(arg, dirName, fileNames):
    for f in fileNames:
        fullPath = os.path.normpath(os.path.join(dirName,f))
        if not os.path.isdir(fullPath):
            ext = os.path.splitext(fullPath)[1]
            if ext in [args.ext]:
                print(fullPath)
                #fo.write(os.path.relpath(fullPath,args.path)+'\n')
                fo.write(fullPath+'\n')
                os.remove(fullPath)
                
fo = open(args.logfile,'w')
os.path.walk(args.path, visit, 1)
fo.close()

