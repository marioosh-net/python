'''
Created on 2010-07-28

@author: marioosh
'''
import sys
# print bez \n 
def p(s):
    'print bez entera'
    sys.stdout.write(s)
def pln(s):
    print(s)
    
class Message:
    # wyswietlanie komunikatow
    @staticmethod
    def debug(m):
        print("DEBUG: " + m)
    @staticmethod
    def info(m):
        print("INFO: " + m)
    @staticmethod
    def error(m):
        print("ERROR: " + m)
        
class Params:
    # pobieranie parametrow
    def __init__(self, minParams, errorMessage):
        self.minParams = minParams
        if len(sys.argv) <= self.minParams:
            print(errorMessage)
            exit()
        self.params = sys.argv[1:]
