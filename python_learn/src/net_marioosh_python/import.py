'''
Created on 2010-07-27

@author: muniek
'''

# import calego modulu
import net.marioosh.python.learn.mymodule as m01
m01.myprint('ala ma kota')

# import wybranych funkcji, mozna teraz ich uzywac BEZ kropki i nazwy modulu
from net.marioosh.python.learn.mymodule import func1, func2
func1()
func2()

# jw., ale import wszystkich funkcji
from net.marioosh.python.learn.mymodule import *
func1()
func2()