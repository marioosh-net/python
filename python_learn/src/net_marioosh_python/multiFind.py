#!/usr/bin/python
# -*- coding: utf-8 -*-
import mimetypes, os, argparse, sys, shutil
    
def visit(arg, dirName, fileNames):
    for f in fileNames:
        fullPath = os.path.normpath(os.path.join(dirName,f))
        if not os.path.isdir(fullPath):
            if f in tab:
                print(fullPath)

                if args.p == False:
                    #copy                    
                    if not os.path.exists(args.dest):
                        os.makedirs(args.dest)
                        
                    if os.path.exists(os.path.join(args.dest,f)):
                        if args.n == False:
                            shutil.copy2(fullPath, args.dest)
                    else:
                        shutil.copy2(fullPath, args.dest)
                    
                    #log
                    if args.p == False:
                        fw = open(args.logfile,'a')
                        fw.write(fullPath+'\n')
                        fw.close()
                    
            
parser = argparse.ArgumentParser('multiFind',description='Multi-search files in Your system');
parser.add_argument('path',nargs='?',default='.',help='searched path, default .');
parser.add_argument('listfile',help='file with list of files to search');
parser.add_argument('dest',nargs='?',default='.',help='destination directory (where files will be copied), default .');
parser.add_argument('logfile',nargs='?',default='multiFind.log',help='log file, default multiFind.log');
parser.add_argument('-p',help='show files only, DON\'T COPY',action='store_true');
parser.add_argument('-n',help='don\'t replace first searched',action='store_true');
args = parser.parse_args(sys.argv[1:]);

fo = open(args.listfile, 'r');
tab = fo.readlines()
fo.close();
i=0
for t in tab:
    tab[i] = tab[i].replace('\n','');
    i += 1
     
os.path.walk(args.path, visit, 1)


