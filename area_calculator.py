# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:26:11 2018

@author: zywuk
"""

from tkinter import *

shaper = ['Circle', 'Triangle', 'Rectangle', 'Trapezoid']
PI = 3.14159
myselect = 0
area_result = 0
interrupt = 0
a=0.0
b=0.0
c=0.0
stringOut = "Cicle radius : 0 cm^2"
calUnit = 1
#default_font = TkFont.nametofont("TkDefaultFont")
#default_font.configure(size=48)

def inputype():
    global myselect, interrupt
    myselect = radio_1.get()
    interrupt = 0
    win_1.destroy()

def cal_fun():
    global interrupt
    interrupt = 0
    win_1.destroy()

def area_cal():
    global a, b, c, area_result, myselect, PI, stringOut, interrupt
    interrupt = 0
    a = ent_1.get()
    if a=="":
        a=0
    else:
        a=float(a)
    b = ent_2.get()
    if b=="":
        b=0
    else:
        b=float(b)
    c = ent_3.get()
    if c=="":
        c=0
    else:
        c=float(c)
    calUnit = radio_unit.get()
    if calUnit == 2:
        a *= 2.54
        b *= 2.54
        c *= 2.54
    if myselect == 0:
        area_result = PI * a * a
        stringOut="Cicle radius : "+ str(a) + " cm"
    elif myselect == 1:
        area_result = 0.5 * a * b
        stringOut="Triangle base : " + str(a) + " cm" +"\n Triangle height : "+ str(b) + " cm"
    elif myselect == 2:
        area_result = a * b
        stringOut="Rectangle width : " + str(a) + " cm" +"\n Rectangle height : "+ str(b) + " cm"
    elif myselect == 3:
        area_result = 0.5 * (a + b)*c
        stringOut="Trapezoid top : " + str(a) + " cm"+"\n Trapezoid bottom : "+ str(b)+ " cm"
        stringOut=stringOut+"\n Trapezoid height : "+str(c)+ " cm"
    win_2.destroy()


while interrupt == 0:
    interrupt = 1
    win_1 = Tk()
    win_1.title('Area Calculator')
    win_1.geometry('+500+300')

    radio_1 = IntVar()
    for i in range(4):
        Radiobutton(win_1, text=shaper[i], variable=radio_1, value=i,
                    width=12, command=inputype).grid(row=0, column=i)
    Label(win_1, text=stringOut).grid(row=3, column=0, 
          columnspan=4)
    Label(win_1, text='the area of shape : ').grid(row=4, column=0, 
          columnspan=2, sticky=E)
    L2 = Label(win_1, text=("%5.2f" %(area_result)+" cm^2"), font='bold')
    L2.grid(row=4, column=2, columnspan=2, sticky=W)
    Button(win_1, text='Calculating', command=cal_fun).grid(row=5, column=0, columnspan=2)
    Button(win_1, text='Exit', command=win_1.destroy).grid(row=5, column=2, columnspan=2)
    radio_1.set(myselect)
    win_1.mainloop()

    if interrupt == 0:
        interrupt = 0
        win_2 = Tk()
        win_2.title('Input.....')
        win_2.geometry('+500+300')
        str_1 = StringVar()
        str_2 = StringVar()
        str_3 = StringVar()
        ent_1 = StringVar()
        ent_2 = StringVar()
        ent_3 = StringVar()
        radio_unit = IntVar()

        if myselect == 0:
            Label(win_2, textvariable = str_1).grid(row=0, column=0)
            Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
            str_1.set('input Radius :')
        elif myselect == 1:
            Label(win_2, textvariable = str_1).grid(row=0, column=0)
            Entry(win_2, textvariable = ent_1).grid(row=0, column=1)
            Label(win_2, textvariable = str_2).grid(row=1, column=0)
            Entry(win_2, textvariable = ent_2).grid(row=1, column=1)
            str_1.set('input base length of Triangel :')
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
        Radiobutton(win_2, text='cm', variable=radio_unit, value=1).grid(row=3, column=0, sticky=E)
        Radiobutton(win_2, text='inch', variable=radio_unit, value=2).grid(row=3, column=1, sticky=W)
        radio_unit.set(calUnit)
        Button(win_2, text='OK', command=area_cal).grid(row=4, column=0, columnspan=2)

        win_2.mainloop()