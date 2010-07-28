'''
Created on 2010-07-27

@author: muniek
'''

# zapis do pliku
f = open('test.txt','w')
f.write('ala ma kotka\ni małego pieska')

# odczyt z pliku
f = open('test.txt','r')

# odczyt po jednej linii
for line in f:
    print(line)

# czy plik istnieje
import os 
if os.path.exists('c:\\zparks.Jpg'):
    print("exist")
else:
    print("not exist")
