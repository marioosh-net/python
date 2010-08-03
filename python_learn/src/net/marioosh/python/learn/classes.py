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
        
    # metoda statyczna nie wymaga domyslnego parametru self
    # i mozna sie do niej odwolywac bez tworzenia obiektu
    # np. KlasaA.separator()
    @staticmethod
    def separator():
        print("-------")    
        
    # metoda prywatna 
    # zaczyna sie od __ (ale NIE konczy __ !!) 
    def __privateMethod(self):
        print('this private method')


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
try:
    a.__privateMethod() # error
except:
    print("private method!")
                


class A:
    def __init__(self):
        print('kontruktor klasy A')
    
class B(A):
    def __init__(self):
        # tutaj trzeba wywolac jawnie superkontruktor
        A.__init__(self)
        print('konstruktor klasy B')
        
class C(A):
    # nie ma zdeklarowanego konstruktora, wiec bedzie wywolany domyslny
    # ktory tez wywola superkontruktor klasy bazowej
    None

print('----')
a = A()
print('----')
b = B()
print('----')
c = C()