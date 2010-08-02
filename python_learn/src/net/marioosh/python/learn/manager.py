'''
Created on 2010-08-02

@author: marioosh
'''
import sqlite3
import argparse
import sys
import os
import subprocess
import getpass

SVNDIR='/var/svn2'
USER = getpass.getuser()

a = argparse.ArgumentParser(prog='manager')
a.add_argument('subsystem', help='subsystem', choices=['svn','mysql','postgres'])
a.add_argument('command', help='komenda', choices=['add','delete','list'])
a.add_argument('params', help='parametry dodatkowe', nargs='?')
args = a.parse_args(sys.argv[1:])

# osbluga svn
if  args.subsystem == 'svn':
    if   args.command == 'add':
        # dodawanie repo
        reponame = args.params
        if reponame != None:
            repopath = os.path.join(SVNDIR,reponame)
            if not os.path.exists(repopath):
                subprocess.call('cd '+SVNDIR+'; svnadmin create '+reponame+'; chown -R '+USER+':svn2 '+reponame+'; chmod -R g+w '+reponame, shell=True)            
            else:
                print ('repo "'+reponame+ '" istnieje!')
        else:
            print ('podaj nazwe repo')
            
    elif args.command == 'delete':
        # usuwanie repo
        reponame = args.params
        if reponame != None:
            repopath = os.path.join(SVNDIR,reponame)
            if os.path.exists(repopath):
                subprocess.call('cd '+SVNDIR+'; rm -rf '+reponame, shell=True)            
            else:
                print ('repo "'+reponame+ '" NIE istnieje!')
        else:
            print ('podaj nazwe repo')
                    
    elif args.command == 'list':
        repolist = os.listdir(SVNDIR)
        for repo in repolist:
            if os.path.isdir(os.path.join(SVNDIR,repo)):
                print(repo)

# osbluga mysql        
elif args.subsystem == 'mysql':
    if   args.command == 'add':
        None
    elif args.command == 'delete':
        None
    elif args.command == 'list':
        None
        
# osbluga postgres        
elif args.subsystem == 'postgres':
    if   args.command == 'add':
        None
    elif args.command == 'delete':
        None
    elif args.command == 'list':
        None
