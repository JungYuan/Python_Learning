# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:25:35 2019

@author: zywuk
"""
from tkinter import *
import math
import time

def star_move(event):
    global a,n,r,step
    x0 = event.x
    y0 = event.y
    star_position = myCan.coords(star) 
    if (x0 < star_position[0]+r) and (x0 > star_position[0]-r):
        if (y0 < star_position[1]) and (y0 > star_position[1]-2*r):
            step = -20
def star_remove(event):
    global a,n,r
    x0 = event.x
    y0 = event.y
    star_position
    b=[x0-r, y0-r, x0+r, y0+r]
    myCan.create_oval(b, fill="#eeeeee", outline="#eeeeee")

mywin = Tk()
myCan = Canvas(mywin, width=500, height=800, bg="#eeeeee")
myCan.pack()

PI = 3.1415926
n, r = 7, 20
x0, y0 = 400, 320
a=[]
for i in range(n):
    x = r*math.cos(2*PI/n*int(n/2)*i+PI/2)
    y = r*math.sin(2*PI/n*int(n/2)*i+PI/2)
    a.append([x,y])
    
myCan.bind("<Button-1>", star_move)
#myCan.bind("<B3-Motion>", star_remove)
star = myCan.create_polygon(a, fill="lightblue")
myCan.move(star, 250, 100)
step = 0
star_position = myCan.coords(star)
while star_position[1] < 800 :
    myCan.move(star, 0, step)
    myCan.update()
    step += 0.5
    if step > 5 :
        step = 5
    time.sleep(0.02)
    star_position = myCan.coords(star)

"""
star = myCan.create_polygon(a, fill="lightblue")
for i in range(100):
    myCan.move(star, 2, 0)
    myCan.update()
    time.sleep(0.01)
"""


mywin.mainloop() 