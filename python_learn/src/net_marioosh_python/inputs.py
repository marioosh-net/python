'''
Created on 2010-07-28

@author: "marioosh"
'''
#
# parametry wejsciowe
#
import sys
print("komenda ze sciezka: " + sys.argv[0])
try:
    print("parametr 1: " + sys.argv[1])
    print("parametr 2: " + sys.argv[2])
except:
    print("brak parametrow wejsciowych")
    
import os
module = os.path.basename(sys.argv[0])
print("nazwa modulu uruchamianego: " + module)

# prosty input
answer = raw_input("podaj odpowiedz: ")

# pobieranie danych w czasie wykonywania skryptu
x = raw_input('Podaj liczbe x: ')
print(x)
try:
    # tak zle (nie mozna laczyc stringow i liczb)
    print(10 + x)
except:
    print("error")

# Can't convert 'int' object to str implicitly
try: print("sss" + 10) 
except: print("error")
# teraz ok
print("sss" + str(10))
# tak ok
print(int(x) + 10)

# podana wartosc musi byc liczbowa (inaczej poleci blad)
mass_kg = int(raw_input("podaj liczbe: " ))
print(mass_kg)

# input vs raw_input
try:
    name = input("What is your name? ")
    print "Hello, " + name + "!"
except:
    # NameError: name 'asdasdas' is not defined
    print('error!')

name = raw_input("What is your name? ")
print "Hello, " + name + "!"