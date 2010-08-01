# -*- coding: iso-8859-2 -*-
'''
Created on 2010-07-31

@author: marioosh
'''

import sqlite3
# utworzenie bazy
conn = sqlite3.connect('/tmp/db1')

# kursor ???
c = conn.cursor()

try:
    # stworzenie tabeli
    c.execute('create table photos (id INTEGER PRIMARY KEY, hash text, path text)')
except:
    print('tabela już istnieje');
    
# insert
c.execute("insert into photos (hash, path) values ('sdsadadsa','/var/www')");

# commit
conn.commit()

# select
hash = ('sdsadadsa',)
c.execute('select * from photos where hash=?', hash)
for row in c:
    print row

# select
hash = ('not exist',)
c.execute('select * from photos where hash=?', hash)
if c.fetchone() == None:
    print('brak rekordu')

# zamkniecie polaczenia
conn.close()
