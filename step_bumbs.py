# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:18:53 2018

@author: zywuk
"""
import tkinter as tk
from tkinter import messagebox
import random as rd
from sys import platform
from datetime import datetime

class isBumb:
    def __init__(self, inWin, rowPos, columnPos):
        self.inWin = inWin
        self.rowPos = rowPos
        self.columnPos = columnPos
        self.inside = tk.StringVar()
        self.idInside = tk.Label(self.inWin, textvariable=self.inside,
                                 font="Arial 12", width=1, height=1,
                                 padx=3, pady=3)
        self.idInside.grid(row=self.rowPos, column=self.columnPos)
        self.id = tk.Button(self.inWin, text="", font="Arial 12",
                            width=2, height=1, pady=2)
        self.id.grid(row=self.rowPos, column=self.columnPos)
        self.id.bind("<Button-1>", self.pressed)
        self.id.bind("<Button-3>", self.marked)
        if platform == "darwin":
            self.id.bind("<Button-2>", self.marked)
        self.checkBumb = False
        self.beMarked = False
    def putIn(self, inside):
        if inside == "B":
            self.inside.set(inside)
            self.idInside["fg"] = "red"
            self.checkBumb = True
        elif inside == "1":
            if self.inside.get() == "":
                self.inside.set("1")
            else:
                a = int(self.inside.get())+1
                self.inside.set(str(a))
    def pressed(self, event):
        if not(self.beMarked) and self.id.grid_info():
            self.id.grid_forget()
            checkId = self.inside.get()
            updat_steped()
            if checkId == "B":
                updat_bumbed()
                tk.messagebox.showwarning("Warning...", "Boom.....\nYou steped on bumb.")
	    	    #self.inWin.destroy()
            elif checkId == "":
                extendPressed(self.rowPos, self.columnPos)
    def marked(self, event):
        if self.beMarked:
            self.beMarked = False
            self.id["text"] = ""
            updat_marked(-1)
        else:
            self.beMarked = True
            self.id["text"] = "X"
            updat_marked(1)
def updat_marked(x):
    marked_num.set(marked_num.get()+x)
    lab_marked["text"] = "Marked : "+str(marked_num.get())+" of 50 bumbs; "
def updat_steped():
    steped_num.set(steped_num.get()+1)
    lab_steped["text"] = "Stepped : "+str(steped_num.get())+" of 256 traps; "
def updat_bumbed():
    bumbed_num.set(bumbed_num.get()+1)
    lab_bumbed["text"] = "Bumbed : "+str(bumbed_num.get())+" of 50 bumbs"
def extendPressed(Bx, By):
    for i in range(-1,2):
        if (((Bx+i) >= 0) and ((Bx+i) <16)):
            for j in range(-1,2):
                if (((By+j) >= 0) and ((By+j) <16)):
                    if (bb[Bx+i][By+j].id.grid_info()):
                        bb[Bx+i][By+j].pressed("<>")
def call_restart():
    global keep_go
    keep_go = 1
    mywin.destroy()
def call_exit():
    global keep_go
    keep_go = 0
    mywin.destroy()

keep_go = 1
def game_1():
    keep_go = 0
    mywin = tk.Tk()
    mywin.title("'Find bumbs'   @by Steven Wu")
    mywin.wm_attributes('-topmost', 1)
    #menu area
    topMenu = tk.Menu(mywin)
    topMenu.add_command(label="Restart", command=call_restart)
    topMenu.add_command(label="Exit", command=call_exit)
    mywin.configure(menu=topMenu)
    #record area
    fr1 = tk.Frame(mywin)
    marked_num = tk.IntVar()
    steped_num = tk.IntVar()
    bumbed_num = tk.IntVar()
    lab_marked = tk.Label(fr1, text="Marked : 0 of 50 bumbs; ")
    lab_steped = tk.Label(fr1, text="Stepped : 0 of 256 traps; ")
    lab_bumbed = tk.Label(fr1, text="Bumbed : 0 of 50 bumbs")
    lab_marked.grid(row=0, column=0)
    lab_steped.grid(row=0, column=1)
    lab_bumbed.grid(row=0, column=2)
    #bumbs area
    fr2 = tk.Frame(mywin)
    fr1.pack(pady=10)
    fr2.pack()
    #Generate buttons
    bb=[]
    for i in range(16):
        bb.append([])
        for j in range(16):
            bb[i].append(isBumb(fr2, i, j))
    #random put 20 bumbs
    B_number = 50
    rd.seed(str(datetime.now()))
    a=[rd.randint(0, 255)]
    for i in range(1, B_number):
        rep = 1
        while rep == 1:
            rep = 0
            ra = rd.randint(0, 255)
            for j in range(i-1):
                if ra == a[j]:
                    rep = 1
        a.append(ra)
    a.sort()
    #bumbs put into isBumb Obj
    for i in range(B_number):
        kr = int(a[i]/16)
        kl = a[i]%16
        bb[kr][kl].putIn("B")
        for j in range(-1,2):
            if (((kr+j) >= 0) and ((kr+j) <16)):
                for jj in range(-1,2):
                    if (((kl+jj) >= 0) and ((kl+jj) <16)):
                        if not(bb[kr+j][kl+jj].checkBumb):
                            bb[kr+j][kl+jj].putIn("1")
    
    mywin.mainloop()

main_win = tk.Tk()
tk.Button(main_win, text="GAME1", command=game_1).pack()
main_win.mainloop()