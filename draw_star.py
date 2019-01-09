#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import math as ma

PI=3.1415926
r = 150
x0, y0 = 240, 180

def draw_polygon():
    global PI, r, x0, y0
    myCan.delete("all")
    n=varN.get()
    x=[0]*n
    y=[0]*n
    for i in range(n):
        x[i]=r*ma.cos(2*PI*i/n+PI/2)
        y[i]=r*ma.sin(2*PI*i/n+PI/2)
    for i in range(n):
        myCan.create_line(x0+x[i%n],y0-y[i%n],x0+x[(i+1)%n],y0-y[(i+1)%n])
        
def draw_star():
    global PI, r, x0, y0
    myCan.delete("all")
    n=varN.get()
    x=[0]*n
    y=[0]*n
    for i in range(n):
        x[i]=r*ma.cos(2*PI*i/n+PI/2)
        y[i]=r*ma.sin(2*PI*i/n+PI/2)
    #draw line
    step = int(n/2)
    first=0
    for i in range(n):  
        second = (first+step)%n
        myCan.create_line(x0+x[first],y0-y[first],x0+x[second],y0-y[second])
        first = second

mywin = Tk()
mywin.title('Tk Demo')

varN= IntVar();
Label(mywin, text="Draw Polygon / Star", font="Arial 16 bold underline").grid(row=0, column=0, columnspan=4, padx=10, pady=10)
Label(mywin, text="Key in number of point : ").grid(row=1, column=0)
Entry(mywin, textvariable=varN).grid(row=1, column=1)
Button(mywin, text="Draw Polygon", command=draw_polygon).grid(row=1, column=2)
Button(mywin, text="Draw Star", command=draw_star).grid(row=1, column=3)

myCan = Canvas(mywin, width=480, height=360, bg="#eeeeee")
myCan.grid(row=2, column=0, columnspan=4)


mywin.mainloop()