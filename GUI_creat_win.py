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

mylabel1 = Label(mywin, text='This is a test label !')
mylabel1.pack(side = LEFT)
mylabel = Label(mywin, text='Hellow, first lebal .....', fg='#ff0000')
mylabel.pack(side = RIGHT)
mylabel = Label(mywin, text='Hellow, first lebal .....', 
                fg='#ff0000', 
                bg="yellow", 
                font="Arial",
                width=20,
                height= 5)
mylabel.pack()
mylabel = Label(mywin, text='吳老師好帥！\n非常帥 !\n帥到分手！', 
                fg='#ff0000', 
                bg="yellow", 
                font="標楷體 32 bold",
                width = 20,
                height = 5,
                anchor ='nw',
                padx=10,
                pady=10,
                justify = RIGHT)
mylabel.pack(fill=X, pady=20)
mylabel1['font'] = 'Arial 18'

mybutton = Button(mywin, text='OK',
                  width = 10,
                  height = 2)
mybutton.pack()

mywin.mainloop()