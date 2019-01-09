import tkinter as tk
from tkinter import messagebox
import random as rd

class isBumb:
    def __init__(self, inWin, rowPos, columnPos):
        self.inWin = inWin
        self.rowPos = rowPos
        self.columnPos = columnPos
        self.inside = tk.StringVar()
        self.idInside = tk.Label(self.inWin, textvariable=self.inside, width=1)
        self.idInside.grid(row=self.rowPos, column=self.columnPos)
        self.id = tk.Button(self.inWin, text="", width=1)
        self.id.grid(row=self.rowPos, column=self.columnPos)
        self.id.bind("<Button-1>", self.pressed)
        self.id.bind("<Button-3>", self.marked)
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
        if not(self.beMarked):
            self.id.grid_forget()
            if self.inside.get() == "B":
                tk.messagebox.showwarning("Warning...", "Boom.....\nYou steped on bumb.")
		    	#self.inWin.destroy()
    def marked(self, event):
        if self.beMarked:
            self.beMarked = False
            self.id["text"] = ""
        else:
            self.beMarked = True
            self.id["text"] = "X"


mywin = tk.Tk()
bb=[]
for i in range(16):
    bb.append([])
    for j in range(16):
        bb[i].append(isBumb(mywin, i, j))
#random put 20 bumbs 
B_number = 50
a=[rd.randint(0, 256)]
for i in range(1, B_number):
    rep = 1
    while rep == 1:
        rep = 0
        ra = rd.randint(0, 256)
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


