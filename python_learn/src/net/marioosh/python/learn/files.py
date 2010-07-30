'''
Created on 2010-07-27

@author: muniek
'''
#
# odczyt z pliku
#
f = open('test.txt','r')
# aktualna pozycja w pliku
print(f.tell())
f.seek(20)
print(f.tell())

# odczyt po jednej linii
for line in f:
    print(line)
print("------------------")    

# odczyt porcjami (np. po 1 znaku)
end = False
f.seek(0)
while not end:
    x = f.read(1)
    if(x != ''):
        print(x)
    else:
        end = True
print("------------------")

#
# zapis do pliku
#
f = open('test.txt','w')
f.write('ala ma kotka\ni malego pieska')

# czy plik istnieje
import os 
if os.path.exists('c:\\zparks.Jpg'):
    print("exist")
else:
    print("not exist")
    
# cos jak find w bashu
print("-------- like find ----------")
import mimetypes
path = raw_input('path: ')
def visit(arg, dirName, fileNames):
    for f in fileNames:
        fullPath = os.path.normpath(os.path.join(dirName,f))
        if not os.path.isdir(fullPath):
            mime = mimetypes.guess_type(fullPath)[0]
            if mime in ['image/jpeg', 'image/gif', 'image/pjpeg']:
                print(fullPath)
os.path.walk(path, visit, 1)