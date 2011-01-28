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

class App:

    def __init__(self, master):

        frame = tkinter.Frame(master, height=200, width=500)
        frame.pack()

        #self.button = tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
        #self.button.pack(side=tkinter.LEFT)

        self.l1 = tkinter.Label(frame, text='File 1')
        self.l1.pack(side=tkinter.LEFT)
        
        self.f1_name = tkinter.Entry(frame)
        self.f1_name.pack(side=tkinter.LEFT)    
        
        self.open_file = tkinter.Button(frame, text="File", command=self.openf)
        self.open_file.pack(side=tkinter.LEFT)        
        
        self.run = tkinter.Button(frame, text="Run", command=self.run)
        self.run.pack(side=tkinter.LEFT)
        
    def say_hi(self):
        print('hi there, everyone!')
        
    def openf(self):
        myfile = f.askopenfilename()
        if myfile != None:
            self.f1_name.insert(0, myfile)
            print(myfile)
            
    def run(self):
        print('pack')
        
root = tkinter.Tk()
app = App(root)
root.mainloop()
