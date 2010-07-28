'''
Created on 2010-07-28

@author: "marioosh"
'''

#
# obsluga bledow
#
class Exceptions:
    
    def __init__(self):
        print("contructor")
        self.error = 1
        
    def test(self):
        while self.error == 1:
            try:
                self.a = int(input("INT: "))
                self.error = 0
            except:
                print("podano wartosc NIEliczbowa")
                self.error = 1
        print("test() end.")
    
    def plus2(self, a):
        x = a + 2
        return x
    
    # wyjatek danego typu
    def test2(self):
        try:
            print (1/self.a)
        except ZeroDivisionError:
            print ("dzielenie przez 0!")
    
e = Exceptions()
e.test()
e.test2()