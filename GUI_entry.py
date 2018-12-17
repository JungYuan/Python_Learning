# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:30:58 2018

@author: zywuk
"""

from tkinter import *
#from tkinter.ttk import *

def Converting():
    lab_3['text']=str(float(ent_lb.get())*0.45359)
    
def QQ():
    mywin.quit

mywin=Tk()

lab_1 = Label(mywin, text='lb', anchor='w', justify=LEFT)
lab_2 = Label(mywin, text='kg', anchor='w', justify=LEFT)
lab_3 = Label(mywin, text='0', width = 20, bg='white', anchor='e')
ent_lb = Entry(mywin, width = 20, justify=RIGHT)
cov_but = Button(mywin, text='Convert', command=Converting)
qui_but = Button(mywin, text="Quit", command=mywin.destroy)

ent_lb.grid(row=0, column=0)
lab_1.grid(row=0, column=1)
lab_3.grid(row=1, column=0)
lab_2.grid(row=1, column=1)
cov_but.grid(row=2, column=0)
qui_but.grid(row=2, column=1)

ent_lb.focus()

mywin.mainloop()
