#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, argparse, sys, shutil
    
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
                        
                    dest = os.path.join(args.dest,f)
                    if os.path.exists(dest):
                        if args.o:
                            if cmp(fullPath, dest) != 0:
                                shutil.copy2(fullPath, args.dest)
                    else:
                        if cmp(fullPath, dest) != 0:
                            shutil.copy2(fullPath, args.dest)
                    
                    #log
                    if args.p == False:
                        fw = open(args.logfile,'a')
                        fw.write(fullPath+'\n')
                        fw.close()
                    
            
parser = argparse.ArgumentParser(os.path.basename(sys.argv[0]),description='Multi-search files in path');
parser.add_argument('path',nargs='?',default='.',help='searched path, default .');
parser.add_argument('listfile',help='list of files to search (as file)');
parser.add_argument('dest',nargs='?',default='.',help='destination directory (where files will be copied), default .');
parser.add_argument('logfile',nargs='?',default='multiFind.log',help='log file, default multiFind.log');
parser.add_argument('-p',help='show files only, DON\'T COPY',action='store_true');
parser.add_argument('-o',help='overwrite first searched with next searches (in destination)',action='store_true');
args = parser.parse_args(sys.argv[1:]);

fo = open(args.listfile, 'r');
tab = fo.readlines()
fo.close();
i=0
for t in tab:
    tab[i] = tab[i].replace('\n','');
    s = tab[i].split('\\')  # win32
    l = len(s);
    s2 = s[l-1];
    s3 = s2.split('/')  # unix
    l2 = len(s3);
    s4 = s3[l2-1];
    # print(s4)
    tab[i] = s4
    i += 1
     
os.path.walk(args.path, visit, 1)


