'''
Created on 2010-08-02

@author: marioosh
'''
import sqlite3
import argparse
import sys
import os
import subprocess

SVNDIR='/var/svn2'

a = argparse.ArgumentParser(prog='manager')
a.add_argument('subsystem', choices=['svn','mysql','postgres'])
a.add_argument('command', help='komenda', choices=['add','delete','list'])
a.add_argument('params', help='parametry dodatkowe', nargs='?')
args = a.parse_args(sys.argv[1:])

if  args.subsystem == 'svn':
    if   args.command == 'add':
        # dodawanie repo
        reponame = args.params
        repopath = os.path.join(SVNDIR,reponame)
        if not os.path.exists(repopath):
            subprocess.call('cd '+SVNDIR+'; svnadmin create '+reponame, shell=True)            
        else:
            print ('repo '+reponame+ ' istnieje!')
    elif args.command == 'delete':
        print 'delete repo'
    elif args.command == 'list':
        print (os.listdir(SVNDIR))
elif args.subsystem == 'mysql':
    if   args.command == 'add':
        print 'add mysql'
    elif args.command == 'delete':
        print 'delete mysql'
elif args.subsystem == 'postgres':
    if   args.command == 'add':
        print 'add postgres'
    elif args.command == 'delete':
        print 'delete postgres'

print(args.params)