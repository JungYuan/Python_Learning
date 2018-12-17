# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:13:06 2018

@author: zywuk
"""

import tkinter as tk
#from tkinter import ttk

def ch_background(swin, scolor):
    swin.configure(bg=scolor)

mywin = tk.Tk()
mywin.title('GUI button design')
mywin.geometry('500x500')

#mylogo= tk.PhotoImage(file="innovationcs.gif")
#giflabel=tk.Label(mywin)
#but_1 = ttk.Button(mywin, text='yellow', foreground='green', command=lambda:ch_background(mywin, "yellow"))
#but_2 = ttk.Button(mywin, text='pink', foregroundg='pink', command=lambda:ch_background(mywin, "pink"))
but_1 = tk.Button(mywin, text='yellow', command=lambda:ch_background(mywin, "yellow"))
but_2 = tk.Button(mywin, text='pink', command=lambda:ch_background(mywin, "pink"))
but_3 = tk.Button(mywin, text='Quick', command=mywin.destroy)

#giflabel.pack()
but_1.pack(anchor='se', side = tk.LEFT)
but_2.pack(anchor='se', side = tk.LEFT, padx=5)
but_3.pack(anchor='se', side = tk.LEFT)

mywin.mainloop()
    