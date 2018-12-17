# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:18:53 2018

@author: zywuk
"""
from tkinter import *
import random as rd

def draw_shape(x0, y0, a, b):
    myCan.create_line(0, y0, 480, y0, arrow=LAST, arrowshape=(10, 15, 5))
    myCan.create_line(x0, 360, x0, 0, arrow=LAST, arrowshape=(10, 15, 5))
    myCan.create_line(x0-a, y0+b, x0+a, y0-b)
    myCan.create_arc(x0-a, y0+b, x0+a, y0-b, extent=180)
    myCan.create_oval(x0-a, y0+b, x0+a, y0-b)
    myCan.create_rectangle(x0-a, y0+b, x0+a, y0-b)
    for i in range(1, 21):
        myCan.create_oval(x0-i*a/20, y0+i*b/20, x0+i*a/20, y0-i*b/20)
        
def move_fun():
    x0=rd.randint(50, 430)
    y0=rd.randint(50, 310)
    a = rd.randint(50, 230)
    b = rd.randint(50, 170)
    myCan.delete('all')
    draw_shape(x0, y0, a, b)
    


mywin = Tk()
#mywin.configure()
x0, y0 = 240, 180
a=100
b=150

myCan = Canvas(mywin, width = 480, height=360)
myCan.pack()
Button(mywin, text='Exit', command=mywin.destroy).pack(pady=5)
Button(mywin, text='Move', command=move_fun).pack()

draw_shape(x0, y0, a, b)
mywin.mainloop()