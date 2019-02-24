# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:50:33 2019

@author: zywuk
"""

from tkinter import *
from tkinter import messagebox
from time import sleep
from random import shuffle, randint

SN=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def go_pressed(i):
    global dx, dy, pazzle_size, pzls, p_pos, empty, lab_sc, score
    row = int(p_pos[i]/pazzle_size)
    col = p_pos[i]%pazzle_size
    moveable = 0
    n = row+1
    if (n < pazzle_size):
        m = n*pazzle_size+col
        if (p_pos[empty] == m): 
            moveable = 'down'
    n = row-1
    if (n >= 0):
        m = n*pazzle_size+col
        if (p_pos[empty] == m): moveable = 'up'
    n = col+1
    if (n < pazzle_size):
        m = row*pazzle_size+n
        if (p_pos[empty] == m): moveable = 'right'
    n = col-1
    if (n >= 0):
        m = row*pazzle_size+n
        if (p_pos[empty] == m): moveable = 'left'
    if moveable != 0:
        score += 1
        lab_sc["text"] = str(score)
        if moveable == 'down':
            pazzle_move(i, 0, 1, 0, dy)
        elif moveable == 'up':
            pazzle_move(i, 0, -1, 0, dy)
        elif moveable == 'right':
            pazzle_move(i, 1, 0, dx, 0)
        elif moveable == 'left':
            pazzle_move(i, -1, 0, dx, 0)
        tmp = p_pos[i]
        p_pos[i] = p_pos[empty]
        p_pos[empty] = tmp
    if check_result():
        messagebox.showinfo("Result", "Conguration ! you spent "+str(score)+" steps !")
        
def check_result():
    global dx, dy, pazzle_size, pzls, p_pos, empty, lab_sc, score
    uwin = True
    for i in range(empty):
        if p_pos[i] != i:
            uwin = False            
    return uwin

def pazzle_move(ID, dir_x, dir_y, step_x, step_y):
    global dx, dy, pazzle_size, pzls, p_pos, empty
    row = int(p_pos[ID]/pazzle_size)
    col = p_pos[ID]%pazzle_size
    if dir_x != 0:
        for j in range(step_x+1):
            pzls[ID].place(x=col*dx+dir_x*j, y=row*dy)
            mywin.update()
            #sleep(0.0002)
    if dir_y != 0:
        for j in range(step_y+1):
            pzls[ID].place(x=col*dx, y=row*dy+dir_y*j)
            mywin.update()
            #sleep(0.0002)
        
def build_pazzle(numbers, wins, logo):
    btn=[]
    for i in range(numbers):
        tmp=Button(mywin, text=logo[i], padx=5, pady=5, font="Courier 14", command=lambda x=i:go_pressed(x))
        btn.append(tmp)
    return btn

def random_pazzle():
    global dx, dy, pazzle_size, pzls, empty, lab_sc, score
    #each position put different card and randomizing
    pos_card = list(range(pazzle_size**2))
    vac = len(pos_card)-1
    for i in range(500):
        row = int(vac/pazzle_size)
        col = vac%pazzle_size
        move = randint(0,3)
        if move == 0:
            n = row-1
            if n >= 0:
                m = n*pazzle_size+col
                pos_card[vac] = pos_card[m]
                pos_card[m] = empty
                vac = m
                print(move, pos_card)
        elif move == 1:
            n = row+1
            if n < pazzle_size:
                m = n*pazzle_size+col
                pos_card[vac] = pos_card[m]
                pos_card[m] = empty
                vac = m
                print(move, pos_card)
        elif move == 2:
            n = col-1
            if n >= 0:
                m = row*pazzle_size+n
                pos_card[vac] = pos_card[m]
                pos_card[m] = empty
                vac = m
                print(move, pos_card)
        elif move == 3:
            n = col+1
            if n < pazzle_size:
                m = row*pazzle_size+n
                pos_card[vac] = pos_card[m]
                pos_card[m] = empty
                vac = m
                print(move, pos_card)
    #put in position to each cards
    for i in range(len(pos_card)):
        p_pos[pos_card[i]] = i

pazzle_size = 4
pn = pazzle_size**2-1
empty = pn
p_pos=[]
for i in range(pazzle_size*pazzle_size):
    p_pos.append(i)
dx=36
dy=45
win_width= dx*pazzle_size
win_height= dy*pazzle_size+60
mywin = Tk()
mywin.configure(width=win_width, height=win_height)
pzls = build_pazzle(pn, mywin, SN)
lab_sc = Label(mywin, text="", pady = 10, 
               font="Courier 20 bold", fg="white", bg="DarkBlue")
score=0
lab_sc["text"]=str(score)
random_pazzle()
for i in range(pn):
    row = int(p_pos[i]/pazzle_size)
    col = p_pos[i]%pazzle_size
    pzls[i].place(x=col*dx, y=row*dy)
lab_sc.place(x=0, y=win_height-57, width=win_width)


mywin.mainloop()