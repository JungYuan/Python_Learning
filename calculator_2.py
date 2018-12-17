# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:21:24 2018

@author: zywuk
"""

import tkinter as tk

gsum = 0
gcal_action = -2 # -2:=, -3:+, -4:-, -5:*, -6:/
gn = 0
g_number = 0
gn_reset = 1
gn_err = 0
def cal_input(aa):
    global gn, gsum, gcal_action, gn_reset, g_number
    if (gn < 1e13) and (aa >= 0):
        if gn_reset == 1:
            gn = 0
            gn_reset = 0
        gn = gn*10 + aa   
        c_lab['text'] = str(gn)
        g_number = 1
    if aa == -1:
        gn = 0
        gsum = 0
        gcal_action = -2
        c_lab['text'] = str(gn)
    if aa < -1 and g_number == 1:
        g_number = 0
        if gcal_action == -3:
            gsum += gn
        elif gcal_action == -4:
            gsum -= gn
        elif gcal_action == -5:
            gsum *= gn
        elif gcal_action == -6:
            if gn == 0:
                c_lab['text'] = "Devided by zero" 
                gsum = 9999999999999999
            else:
                gsum /= gn
        elif gcal_action == -2:
            gsum = gn
        if gsum < 1e13:
            c_lab['text'] = str(gsum)
            gcal_action = aa
            gn = 0
        elif gsum == 9999999999999999:
            gcal_action = -2
            gn = 0
            gsum = 0
        else:    
            c_lab['text'] = "Over Maximum"
            gcal_action = -2
            gn = 0
            gsum = 0
    elif aa < -1 and g_number == 0:
        gcal_action = aa
        
"""            
            if gn_reset == 0:
                gsum = gn
        if gsum < 1e13:
            if (gsum - int(gsum)) == 0:
                c_lab['text'] = str(int(gsum))
            else:
                c_lab['text'] = str('%13.5f' % (gsum))
        else:
            c_lab['text'] = 'Over Maximum'
        gcal_action = aa
        gn_reset = 1
"""        

"""
    if aa == -3:
        if gcal_action == -3:
            gsum = gsum + gn
            c_lab['text'] = str(gsum)
        gcal_action = aa
"""


mywin=tk.Tk()
mywin.title('Calculator')
mywin.configure(bg='#000000')
mywin.resizable(width=False, height=False)

                
c_lab=tk.Label(mywin, bg='#eeeeee', font='Arial 32',
               width=14,
               bd=3, relief='sunken',
               anchor='e', justify=tk.RIGHT,text=str(gn),
               pady=5,padx=3)
butt_0=tk.Button(mywin, text='0', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(0))
butt_1=tk.Button(mywin, text='1', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(1))
butt_2=tk.Button(mywin, text='2', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(2))
butt_3=tk.Button(mywin, text='3', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(3))
butt_4=tk.Button(mywin, text='4', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(4))
butt_5=tk.Button(mywin, text='5', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(5))
butt_6=tk.Button(mywin, text='6', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(6))
butt_7=tk.Button(mywin, text='7', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(7))
butt_8=tk.Button(mywin, text='8', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(8))
butt_9=tk.Button(mywin, text='9', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(9))
butt_c=tk.Button(mywin, text='C', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(-1))
butt_a=tk.Button(mywin, text='+', width=5, pady=3, font='Calibri 24 bold', command = lambda:cal_input(-3))
butt_m=tk.Button(mywin, text='-', width=5, pady=3, font='Calibri 24 bold', command = lambda:cal_input(-4))
butt_x=tk.Button(mywin, text='X', width=5, pady=3, font='Calibri 24 bold', command = lambda:cal_input(-5))
butt_d=tk.Button(mywin, text='/', width=5, pady=3, font='Calibri 24 bold', command = lambda:cal_input(-6))
butt_e=tk.Button(mywin, text='=', width=5, pady=3, font='Calibri 24', command = lambda:cal_input(-2))


c_lab.grid(row=0, column =0, columnspan=4)
butt_7.grid(row=1, column =0)
butt_8.grid(row=1, column =1)
butt_9.grid(row=1, column =2)
butt_a.grid(row=1, column =3)
butt_4.grid(row=2, column =0)
butt_5.grid(row=2, column =1)
butt_6.grid(row=2, column =2)
butt_m.grid(row=2, column =3)
butt_1.grid(row=3, column =0)
butt_2.grid(row=3, column =1)
butt_3.grid(row=3, column =2)
butt_x.grid(row=3, column =3)
butt_c.grid(row=4, column =0)
butt_0.grid(row=4, column =1)
butt_e.grid(row=4, column =2)
butt_d.grid(row=4, column =3)

mywin.mainloop()