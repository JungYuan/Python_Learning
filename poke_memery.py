# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:26:26 2019

@author: zywuk
"""

from tkinter import *
from random import shuffle
from time import sleep
from tkinter import messagebox

turn = 0
open_no = 0
open_card = [0, 0]
def go_open(num):
    global turn, open_no, card_kind, card_point, pokes, pokes_no, score, player
    global def_color, player_name
    open_no += 1
    if open_no == 2 and open_card[0]==num :
        open_no -= 1
        return
    pokes[num]["bg"]="White"
    kind=int(pokes_no[num]/13)
    point=pokes_no[num]%13
    if kind < 2:
        pokes[num]["fg"]="Black"
    else:
        pokes[num]["fg"]="Red"
    pokes[num]["text"]=card_kind[kind]+card_point[point]
    mywin.update()
    open_card[open_no-1]=num
    if open_no == 2:
        sleep(1)
        if check_point(open_card):
            score[turn].set(score[turn].get()+1)
            pokes[open_card[0]]["bg"]=player_color[turn]
            pokes[open_card[1]]["bg"]=player_color[turn]
            pokes[open_card[0]]["command"]=""
            pokes[open_card[1]]["command"]=""
            if score[0].get()+score[1].get() == 26:
                msg = "the winner is "
                if score[0].get()==score[1].get():
                    messagebox.showinfo("Result", "No one win this game. Result is even !")
                elif score[0].get() > score[1].get():
                    messagebox.showinfo("Result", msg+player_name[0]+" !")
                else:
                    messagebox.showinfo("Result", msg+player_name[1]+" !")
        else:
            sleep(2)
            go_close(open_card)
            turn = (turn+1)%2
        if turn == 0:
            player[0]["bg"]="DarkGreen"
            player[1]["bg"]=def_color
        else:
            player[0]["bg"]=def_color
            player[1]["bg"]="DarkGreen"
        open_no = 0
        

def go_close(oc):
    for i in range(2):
        pokes[oc[i]]["bg"] = "LightSeaGreen"
        pokes[oc[i]]["text"] = "҉"
        pokes[oc[i]]["fg"] = "Blue"

def check_point(oc):
    global card_point, pokes_no
    getpoint = False
    if (pokes_no[oc[0]]%13) == (pokes_no[oc[1]]%13): getpoint=True
    return getpoint

mywin=Tk()
player = [1,2]
player_name=["Master", "Challanger"]
player_color=["LightBlue", "LightPink"]
card_kind=["♠\n", "♣\n", "♥\n", "♦\n"]
card_point = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
pokes=list(range(52))
pokes_no=list(range(52))
shuffle(pokes_no)

score = [IntVar(), IntVar()]
player[0] = Button(mywin, text=player_name[0], font="Arial 20",
                   width=12, pady=5, relief="sunken", bd=2, fg=player_color[0])
player[1] = Button(mywin, text=player_name[1], font="Arial 20",
                   width=12, pady=5, relief="sunken", bd=2, fg=player_color[1])
player[0].grid(row=0, column=0, rowspan=2, sticky="n")
player[1].grid(row=0, column=14, rowspan=2, sticky="n")
for i in range(4):
    for j in range(13):
        k=i*13+j
        pokes[k]=Button(mywin, text="҉", fg="Blue", bg="LightSeaGreen",
                        width=2, height=2, padx=2, pady=3,
                        font="Courier 14", command=lambda x=k:go_open(x))
        pokes[k].grid(row=i, column=1+j)
Label(mywin, textvariable=score[0], font="Courier 24").grid(row=2, column=0, rowspan=2)
Label(mywin, textvariable=score[1], font="Courier 24").grid(row=2, column=14, rowspan=2)
def_color=player[0]["bg"]
player[0]["bg"]="DarkGreen"

mywin.mainloop()

    