'''
Created on 2010-07-27

@author: muniek
'''

# dziedziczy z object, dlatego rownoznaczne to jest z 
# class KlasaA(object):
class KlasaA:

    # konstruktor (MOZE BYC TYLKO JEDEN!)
    def __init__(self):
        print("KlasaA()")
    
    # przesloniecie toString 
    def __str__(self):
        return "toString: " + object.__str__(self)
    
    def test(self):
        print('test > ' + str(self))
        


# dziedziczenie z klasy A 
class KlasaB(KlasaA):

    # konstruktor z parametrami
    def __init__(self, a):
        self.a = a
        print("KlasaB(" + a + ")")


a = KlasaA();
print(a)
b = KlasaB('dupa jas');
c = KlasaB('jasiek');
print(b)
b.test()
a.test()
                