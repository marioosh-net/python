'''
Created on 2010-07-29

@author: marioosh
'''

# standardowa funkcja
def nazwaFunkcji(param1, param2='dupa'):
    'opis funkcji'
    print(param1),
    print(param2)

nazwaFunkcji('ala')
nazwaFunkcji('ala',param2='ciao')
nazwaFunkcji(param2='ala',param1='ciao')

# funkcja z dowolna liczba parametrow
def multi(*params):
    for param in params:
        print(param),
        
multi('ala','ola','tomek','wacek')

# funckja anonimowa
def dajFunkcje(n):
    return lambda n: n+5

dajFunkcje(10)
