'''
Created on 2010-07-28

@author: "marioosh"
'''

# 
# Python wrapper for Tcl/Tk,
# 
import tkinter
import tkinter.filedialog as f
import tkinter.messagebox as m
import os, sys, shutil
import subprocess


class App:

    def __init__(self, master):

        frame = tkinter.Frame(master, height=100, width=300)
        frame.pack()
        #frame.pack_propagate(0)

        #self.button = tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
        #self.button.pack(side=tkinter.LEFT)

        self.messages = tkinter.Label(frame, text='')
        self.messages.pack(side=tkinter.TOP)        

        self.l1 = tkinter.Label(frame, text='File 1')
        self.l1.pack(side=tkinter.LEFT)
        
        self.f1_name = tkinter.Entry(frame)
        self.f1_name.pack(side=tkinter.LEFT)    

        self.open_file = tkinter.Button(frame, text="File", command=self.openf)
        self.open_file.pack(side=tkinter.LEFT)        
        
        self.l1 = tkinter.Label(frame, text='Password')
        self.l1.pack(side=tkinter.LEFT)
        
        self.passw = tkinter.Entry(frame)
        self.passw.pack(side=tkinter.LEFT)    
        
        self.run = tkinter.Button(frame, text="Run", command=self.run)
        self.run.pack(side=tkinter.LEFT)
        
        self.myfile = None
        
    def openf(self):
        self.myfile = f.askopenfilename()
        self.f1_name.insert(0, self.myfile)
            
    def run(self):
        if self.myfile != None:
            if len(self.passw.get()) > 0:
                self.messages.configure(text='')
                self.f1_name.insert(0, self.myfile)
                print(self.myfile)
                
                self.process();                
                
            else:
                self.messages.configure(text='Error: Input password')
        else:
            self.messages.configure(text='Error: Select file')

    def process(self):
        zipfile = self.f2zip(self.myfile)
        # zaczytaj sciezke do drugiego pliku z configa
        f3 = open('zipper.conf')
        file2 = f3.readline()
        file2 = file2.strip()
        
        # katalog glowny na zipy
        dir = self.myfile+'_dir'
        self.make_or_del(dir)
    
        zip1dir = os.path.normpath(os.path.join(dir,'zip1'))
        zip2dir = os.path.normpath(os.path.join(dir,'zip2'))
        zip3dir = os.path.normpath(os.path.join(dir,'zip3'))
        os.mkdir(zip1dir)
        os.mkdir(zip2dir)
        os.mkdir(zip3dir)
        
        # password = getpass.getpass('Password: ')
        password = self.passw.get()
    
        # pakuj 7-zipem
        pz1 = os.path.normpath(os.path.join(zip1dir,zipfile))
        subprocess.call(['7z', 'a', '-y', pz1] + [self.myfile])
        pz2 = os.path.normpath(os.path.join(zip2dir,zipfile))
        subprocess.call(['7z', 'a', '-p'+password, '-y', pz2] + [self.myfile])
        pz3 = os.path.normpath(os.path.join(zip3dir,zipfile))
        subprocess.call(['7z', 'a', '-p'+password, '-y', pz3] + [self.myfile,file2])
        
        print(pz1)
        print(pz2)
        print(pz3)
        
        
    # jak jest katalog to go usun
    def make_or_del(self,path):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)
    
    # rozszerzenie na .zip
    def f2zip(self,f):
        x = os.path.basename(f)
        return os.path.splitext(x)[0] + ".zip"

        
root = tkinter.Tk()
app = App(root)
root.mainloop()
