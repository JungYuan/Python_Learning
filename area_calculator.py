# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:26:11 2018

@author: zywuk
"""

from tkinter import *

shaper = ['Circle', 'Triangle', 'Rectangle', 'Trapezoid']
myselect = 0

def inputype():
    global myselect
    myselect = radio_1.get()
    win_1.destroy()

def area_cal():
    pass


win_1 = Tk()
win_1.title('Area Calculator')
win_1.geometry('+500+300')


radio_1 = IntVar()

for i in range(4):
    Radiobutton(win_1, text=shaper[i], variable=radio_1, value=i, 
                width=12, command=inputype).grid(row=0, column=i)

Button(win_1, text='Calculating', command=area_cal).grid(row=3, column=0, columnspan=2)
Button(win_1, text='Exit', command=win_1.destroy).grid(row=3, column=2, columnspan=2)

win_1.mainloop()
win_2 = Tk()
win_2.title('Input.....')
win_2.geometry('+500+300')
str_1 = StringVar()
str_2 = StringVar()
str_3 = StringVar()
ent_1 = DoubleVar()
ent_2 = DoubleVar()
ent_3 = DoubleVar()

if myselect == 0:
    Label(win_2, textvariable = str_1).grid(row=0, column=0)
    Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
    str_1.set('input Radius :')
elif myselect == 1:
    Label(win_2, textvariable = str_1).grid(row=0, column=0)
    Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
    Label(win_2, textvariable = str_2).grid(row=1, column=0)
    Entry(win_2, textvariable = ent_2).grid(row=1, column=1)
    str_1.set('input base length of Traiangel :')
    str_2.set('input Height of Traiangel :')
elif myselect == 2:
    Label(win_2, textvariable = str_1).grid(row=0, column=0)
    Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
    Label(win_2, textvariable = str_2).grid(row=1, column=0)
    Entry(win_2, textvariable = ent_2).grid(row=1, column=1)
    str_1.set('input width of Rectangle :')
    str_2.set('input Height of Rectangel :')
elif myselect == 3:
    Label(win_2, textvariable = str_1).grid(row=0, column=0)
    Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
    Label(win_2, textvariable = str_2).grid(row=1, column=0)
    Entry(win_2, textvariable = ent_2).grid(row=1, column=1)
    Label(win_2, textvariable = str_3).grid(row=2, column=0)
    Entry(win_2, textvariable = ent_3).grid(row=2, column=1)
    str_1.set('input top length of Trapezoid :')
    str_2.set('input bottom length of Trapezoid :')
    str_3.set('input height of Trapezoid :')
    
Button(win_2, text='OK', command=win_2.destroy).grid(row=4, column=0, columnspan=2)
win_2.mainloop()


