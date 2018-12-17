# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:21:32 2018

@author: zywuk
"""

from tkinter import *
from numpy import *

aa=''
cont = 1
PI = 3.1415926535897932384626
def show_cal(*args):
    my_lab.set(my_ent.get())

def calculat():
    global PI, aa, cont
    formula = my_ent.get()
    if formula == 'exit':
        cont = 0
    else:
        aa = formula + " = " + str(eval(formula))
    mywin.destroy()
    
while cont == 1:    
    mywin = Tk()
    my_ent = StringVar()
    my_lab = StringVar()
    Entry(mywin, width=100, textvariable=my_ent).pack()
    Label(mywin, textvariable = my_lab).pack()
    Button(mywin, text = "Answer", command=calculat).pack()
    my_lab.set('Calculating..') 
    my_ent.trace('w', show_cal)

    mywin.mainloop()
    if cont == 1:
        ans_win = Tk()
        Label(ans_win, text=aa).pack()
        Button(ans_win, text='OK', command=ans_win.destroy).pack()
        ans_win.mainloop()