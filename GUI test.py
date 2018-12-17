# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:57:48 2018

@author: zywuk
"""
from tkinter import *

mywin = Tk()
mywin.title("Steven's window")
max_x=mywin.winfo_screenwidth()
max_y=mywin.winfo_screenheight()
w_width = 500 #int(max_x/2)
w_height = 500 #int(max_y/2)
p_x = int((max_x-w_width)/2)
p_y = int((max_y-w_height)/2)
#mywin.configure(width=max_x, height=max_y,background='#eeee33')
mywin.geometry('%dx%d+%d+%d' %(w_width, w_height, p_x, p_y))

mywin.mainloop()