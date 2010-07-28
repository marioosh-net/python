'''
Created on 2010-07-27

@author: marioosh
'''
# from net.marioosh.python.learn.log import Log
from log import Log

#
# if else...
#
a = 6
b = 7
c = 42
print (1, a == 6)
print (3, a == 6 and b == 7)

# if elese
if a > 4:
    print("a > 4")
else:
    print("a <= 4")

# if elseif 
if a > 4:
    print("a > 4")
elif a > 6:
    print("a > 6")
else:
    print("a <= 4")
Log.separator() 

#
# print
#
print("ala ma kota")
# skladanie tekstu
print("ala ma kota","dupa jas","wacek","...")
print("ala ma kota"+"dupa jas"+"wacek"+"...")
#
import sys
print ("syntax: ...", None , None , sys.stderr) 
Log.separator()

#
# operacje matematyczne
#
a = 2
print(a)
import math
print (math.sin(31))
Log.separator()

#
# stringi
#
s = 'ALA ma kota'
print(len(s))   # len() dlugosc stringa
print(s)
print(s.lower())

string1 = 'ala ma kotka" '
print(string1.strip())
Log.separator()

#
# listy
#
s = [];
s.append("sdsds");
s.append("sdsds");
s.append("sdsds");s.append("sdsds");
for i in s: 
    print(i);
print(('kk'))
Log.separator()
