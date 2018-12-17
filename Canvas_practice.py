# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:02:53 2018

@author: zywuk
"""

from tkinter import *
import math
import random 

def can_cls():
    can1.delete('all')

def draw_rect():
    can1.delete("all")
    for i in range(50):
        x1, x2 = random.randint(1,480), random.randint(1,480)
        if x1 > x2 :
            x1, x2 = x2, x1 
            # a = x1
            # x1 = x2
            # x2 = a
        y1, y2 = random.randint(1,360), random.randint(1,360)
        if y1 > y2 :
            y1, y2 = y2, y1 
        can1.create_rectangle(x1, y1, x2, y2)

def draw_line():
    can1.delete('all')
    x_center, y_center, r = 240, 180, 100
    x, y = [],[]
    for i in range(12):
        x.append(x_center+r*math.cos(30*i*math.pi/180))
        y.append(y_center+r*math.sin(30*i*math.pi/180))
    for i in range(12):
        for j in range(12):
            can1.create_line(x[i],y[i],x[j],y[j], width=1)

def draw_oval():
    can1.delete("all")
    dw, dh = 12, 9
    x1, y1 = random.randint(50,430), random.randint(50,310)
    #x1, y1 = 240, 180
    dx = x1/40.0
    dy = y1/40.0
    for i in range(40):
        x1 = x1 - dx
        y1 = y1 - dy
        x2 = x1 + dw * (i+1)
        y2 = y1 + dh * (i+1)
        can1.create_oval(x1, y1, x2, y2)    

mywin = Tk()
mywin.title('paint')

fr1 = Frame(mywin)
fr2 = Frame(mywin)
can1 = Canvas(fr1, width=480, height=360)
can1.pack()
Button(fr2, text="Line", command=draw_line).grid(row=0, column=0)
Button(fr2, text="Rectangle", command=draw_rect).grid(row=0, column=1)
Button(fr2, text="Oval", command=draw_oval).grid(row=0, column=2)
Button(fr2, text='clear', command=can_cls).grid(row=0, column=5)

fr1.pack()
fr2.pack()

mywin.mainloop()