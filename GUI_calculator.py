# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:06:05 2018

@author: zywuk
"""

import tkinter as tk

gn = 0
gsum = 0
gcal = 0  #=:0, +:1, -:2, x:3, /:4
def calculate(n):
    global gn
    if n < 0 :
        gn = 0
        gsum = 0
        gcal = 0
    elif gn < 1E12:
        gn = gn*10 + n
    c_lab['text']=str(gn)
    
def cal_sum(ff):
    global gn, gsum, gcal
    if gcal == 0:
        gsum = gn
    elif gcal == 1:
        gsum += gn
    elif gcal == 2:
        gsum -= gn
    elif gcal == 3:
        gsum *= gn
    else:
        gsum /= gn
    gcal = ff
    gn = 0
    c_lab['text']=str(gsum)
    
mywin=tk.Tk()
mywin.title('Calculator')
mywin.configure(bg='#000000')
mywin.resizable(width=False, height=False)

mybut=[tk.Button]*10
                
c_lab=tk.Label(mywin, bg='#eeeeee', font='Arial 27',
               width=14,
               bd=3, relief='sunken',
               anchor='e', justify=tk.RIGHT,text=str(0),
               pady=5,padx=3)
butt_9=tk.Button(mywin, text='9', width=5, pady=3, command=lambda:calculate(9), font='Calibri 20')
butt_8=tk.Button(mywin, text='8', width=5, pady=3, command=lambda:calculate(8), font='Calibri 20')
butt_7=tk.Button(mywin, text='7', width=5, pady=3, command=lambda:calculate(7), font='Calibri 20')
butt_6=tk.Button(mywin, text='6', width=5, pady=3, command=lambda:calculate(6), font='Calibri 20')
butt_5=tk.Button(mywin, text='5', width=5, pady=3, command=lambda:calculate(5), font='Calibri 20')
butt_4=tk.Button(mywin, text='4', width=5, pady=3, command=lambda:calculate(4), font='Calibri 20')
butt_3=tk.Button(mywin, text='3', width=5, pady=3, command=lambda:calculate(3), font='Calibri 20')
butt_2=tk.Button(mywin, text='2', width=5, pady=3, command=lambda:calculate(2), font='Calibri 20')
butt_1=tk.Button(mywin, text='1', width=5, pady=3, command=lambda:calculate(1), font='Calibri 20')
butt_0=tk.Button(mywin, text='0', width=5, pady=3, command=lambda:calculate(0), font='Calibri 20')
butt_c=tk.Button(mywin, text='C', width=5, pady=3, command=lambda:calculate(-1), font='Calibri 20')
butt_a=tk.Button(mywin, text='+', width=5, pady=3, command=lambda:cal_sum(1), font='Calibri 20 bold')
butt_m=tk.Button(mywin, text='-', width=5, pady=3, command=lambda:cal_sum(2), font='Calibri 20 bold')
butt_t=tk.Button(mywin, text='x', width=5, pady=3, command=lambda:cal_sum(3), font='Calibri 20 bold')
butt_d=tk.Button(mywin, text='/', width=5, pady=3, command=lambda:cal_sum(4), font='Calibri 20 bold')
butt_e=tk.Button(mywin, text='=', width=5, pady=3, command=lambda:cal_sum(0), font='Calibri 20 bold')

c_lab.grid(row=0, column=0, columnspan=4, pady=5)
butt_9.grid(row=1, column=2)
butt_8.grid(row=1, column=1)
butt_7.grid(row=1, column=0)
butt_6.grid(row=2, column=2)
butt_5.grid(row=2, column=1)
butt_4.grid(row=2, column=0)
butt_3.grid(row=3, column=2)
butt_2.grid(row=3, column=1)
butt_1.grid(row=3, column=0)
butt_c.grid(row=4, column=0)
butt_0.grid(row=4, column=1)
butt_a.grid(row=1, column=3)
butt_m.grid(row=2, column=3)
butt_t.grid(row=3, column=3)
butt_d.grid(row=4, column=3)
butt_e.grid(row=4, column=2)

                
mywin.mainloop()