# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:09:43 2018

@author: zywuk
"""

import tkinter as tk

mywin = tk.Tk()
mywin.title('GUI design class')
mylb_1 = tk.Label(mywin, text="label 1 green", font='Arial 12',
               bg = 'green', fg = "#ff0000",
               padx = 5, pady = 5)
mylb_2 = tk.Label(mywin, text="blue label 2", font='Arial 12',
               bg = 'blue', fg = "#eeeeee",
               padx = 5, pady = 5)
mylb_3 = tk.Label(mywin, text="brown label 3", font='Arial 12',
               bg = 'brown', fg = "yellow",
               padx = 5, pady = 5)
mylb_1.grid(row = 0, column = 0)
mylb_2.grid(row = 1, column = 1, padx = 10)
mylb_3.grid(row = 2, column = 2)


mywin.mainloop()