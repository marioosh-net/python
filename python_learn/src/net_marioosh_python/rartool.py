'''
Created on 2010-07-28

@author: "marioosh"
'''

# 
# Python wrapper for Tcl/Tk,
# 
import Tkinter as tkinter
import tkFileDialog as f
# 3.1
# import tkinter as tkinter
# from tkinter import filedialog as f
# import Tkinter.messagebox as m
import os, sys, shutil
import subprocess


class App:

    def __init__(self, master):
        
        # plik konfiguracyjny
        self.configfile = 'zipper.conf';

        frame = tkinter.Frame(master, padx=10, pady=10)
        # print(frame.keys())
        frame.grid()
        # frame.grid_propagate(0)

        self.messages = tkinter.Label(frame, text='')
        self.messages.grid(row=0,columnspan=3)

        self.l1 = tkinter.Label(frame, text='File 1')
        self.l1.grid(row=1,column=0,sticky='E')
        self.f1_name = tkinter.Entry(frame,width=40)
        self.f1_name.grid(row=1,column=1)
        self.open_file = tkinter.Button(frame, text="Choose", command=self.openf)
        self.open_file.grid(row=1,column=2,sticky='W')
 
        self.l2 = tkinter.Label(frame, text='File 2')
        self.l2.grid(row=2,column=0,sticky='E')
        self.f2_name = tkinter.Entry(frame,width=40)
        self.f2_name.grid(row=2,column=1)    
        self.myfile2 = None
        if not os.path.exists(self.configfile):
            f = open(self.configfile,'w')
            f.write('test.txt\n')
            f.write('{filename}-packed.rar\n')
            f.close()
        f3 = open(self.configfile)

		# plik w 1-szej linii
        file2 = f3.readline()
        file2 = file2.strip()
		# maska w drugiej linii konfiga
		# maska = {filename}{ext}
        mask1 = f3.readline()
        mask1 = mask1.strip()
        f3.close();
				
        self.f2_name.delete(0, tkinter.END)
        self.f2_name.insert(0, file2)
        self.myfile2 = file2

        self.open_file2 = tkinter.Button(frame, text="Choose", command=self.openf2)
        self.open_file2.grid(row=2,column=2,sticky='W')        

        self.lmask = tkinter.Label(frame, text='Mask').grid(row=3,column=0,sticky='E')
        self.mask = tkinter.Entry(frame, width=30)
        self.mask.grid(row=3,column=1,sticky='W')
        self.mask.delete(0, tkinter.END)
        self.mask.insert(0, mask1)

        self.l1 = tkinter.Label(frame, text='Password').grid(row=4,column=0,sticky='E')
        self.passw = tkinter.Entry(frame, show='*', width=30)
        self.passw.grid(row=4,column=1,sticky='W')

        self.run = tkinter.Button(frame, text="Run", command=self.run)
        self.run.grid(row=5,column=1,sticky='w')
        
        self.myfile = None
        
    def openf(self):
        self.myfile = f.askopenfilename()
        self.f1_name.delete(0, tkinter.END)
        self.f1_name.insert(0, self.myfile)
           
    def openf2(self):
        self.myfile2 = f.askopenfilename()
        self.f2_name.delete(0, tkinter.END)
        self.f2_name.insert(0, self.myfile2)
        self.save()

    def save(self):
        fd = open(self.configfile,'w')
        fd.write(self.myfile2+'\n')
        fd.write(self.mask.get())
        fd.close()
       
    def run(self):
        if not len(self.mask.get().strip()) > 0:
            self.messages.configure(text='Error: Input mask')
        else:
            if self.myfile2 != None and len(self.myfile2) > 0:
           
                if self.myfile != None and len(self.myfile) > 0:
                    if len(self.passw.get()) > 0:
                        self.messages.configure(text='')
                        self.f1_name.insert(0, self.myfile)
                        print(self.myfile)

                        self.save()
                        self.process();                
                    else:
                        self.messages.configure(text='Error: Input password')
                else:
                    self.messages.configure(text='Error: Select file')
            else:
                self.messages.configure(text='Error: Select file')
            

    def process(self):
        zipfile = self.f2zip(self.myfile)
        file2 = self.myfile2
        
        # katalog glowny na zipy
        dir = self.myfile+'_dir'
        self.make_or_del(dir)
    
        zip1dir = os.path.normpath(os.path.join(dir,'rar1'))
        zip2dir = os.path.normpath(os.path.join(dir,'rar2'))
        zip3dir = os.path.normpath(os.path.join(dir,'rar3'))
        os.mkdir(zip1dir)
        os.mkdir(zip2dir)
        os.mkdir(zip3dir)
        
        # password = getpass.getpass('Password: ')
        password = self.passw.get()
   
        # pakuj 7-zipem
        # pz1 = os.path.normpath(os.path.join(zip1dir,zipfile))
        # subprocess.call(['7z', 'a', '-y', pz1] + [self.myfile])
        # pz2 = os.path.normpath(os.path.join(zip2dir,zipfile))
        # subprocess.call(['7z', 'a', '-p'+password, '-y', pz2] + [self.myfile])
        # pz3 = os.path.normpath(os.path.join(zip3dir,zipfile))
        # subprocess.call(['7z', 'a', '-p'+password, '-y', pz3] + [self.myfile,file2])
 
        # pakuj rarem
        pz1 = os.path.normpath(os.path.join(zip1dir,zipfile))
        subprocess.call(['rar', 'a', '-r', pz1] + [self.myfile])
        pz2 = os.path.normpath(os.path.join(zip2dir,zipfile))
        subprocess.call(['rar', 'a', '-r', '-p'+password, pz2] + [self.myfile])
        pz3 = os.path.normpath(os.path.join(zip3dir,zipfile))
        subprocess.call(['rar', 'a', '-r', '-p'+password, pz3] + [self.myfile,file2])
        
    # jak jest katalog to go usun
    def make_or_del(self,path):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)
    
    # zwraca nazwe archiwum wg maski
    def f2zip(self,f):
        x = os.path.basename(f)
        filename = os.path.splitext(x)[0];
        ext = os.path.splitext(x)[1];
        rarfile = self.mask.get();
        rarfile = rarfile.replace('{filename}', filename);
        rarfile = rarfile.replace('{ext}', ext);
        return rarfile

        
root = tkinter.Tk()
app = App(root)
root.mainloop()
