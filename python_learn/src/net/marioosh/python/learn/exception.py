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
                int(input("INT: "))
                self.error = 0
            except:
                print("podano wartosc NIEliczbowa")
                self.error = 1
        print("test() end.")
    
e = Exceptions()
e.test()