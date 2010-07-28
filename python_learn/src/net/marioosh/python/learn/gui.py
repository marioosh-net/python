'''
Created on 2010-07-28

@author: "marioosh"
'''

# 
# Python wrapper for Tcl/Tk,
# 
import tkinter as Tkinter
app_win = Tkinter.Tk()
# Create label ob    ject
app_label = Tkinter.Label(app_win,text="Hello World")
app_label.pack()
# Create User Input Object
app_entry = Tkinter.Entry(app_win)
app_entry.pack()
# Create Button Object
app_button = Tkinter.Button(app_win,text="Print Value")
app_button.pack()
app_win.mainloop()
