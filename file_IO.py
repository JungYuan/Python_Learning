# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:05:51 2018

@author: zywuk
"""
from tkinter import *

u_name=[]
u_pwd=[]


def fun_login():
    global u_name, u_pwd
    un=ent_1.get()+'\n'
    upd=ent_2.get()+'\n'
    resp='Username is uncorrect!'
    for i in range(len(u_name)):
        if un == u_name[i]:
            resp='Passwoed is uncorrect !'
            if upd == u_pwd[i]:
                resp='Successful login !'
            break
    ent_1.set('')
    ent_2.set('')
    lab.set(resp)
        

def fun_signin():
    global open_win2
    open_win2 = 1
    win_1.destroy()
    
def add_user():
    global user_file, u_name, u_pwd
    new_user=ent_1.get()+'\n'
    new_pwd=ent_2.get()+'\n'
    resp='Username was added!'
    some_error = 0
    for i in range(len(u_name)):
        if new_user == u_name[i]:
            some_error = 1
            resp='Username is exist. Can\'t sign again '
            break
    lab.set(resp)
    if some_error == 0:
        ###save_file(new_user, new_pwd)
        f = open(user_file, 'w')
        f.write(new_user)
        f.write(new_pwd)
        f.close()
        u_name.append(new_user)
        u_pwd.append(new_pwd)
        win_2.destroy()
    

user_file = 'test.txt'
f = open(user_file, 'a')
r_end = 0
while r_end == 0:
    a=f.readline()
    if a=='':
        r_end=1
    else:
        u_name.append(a)
        u_pwd.append(f.readline())
f.close()

win_1=Tk()
win_1.title('Login')
open_win2 = 0
fr_1=Frame(win_1)
fr_2=Frame(win_1)
ent_1=StringVar()
ent_2=StringVar()
lab=StringVar()
Label(fr_1, text="User name :").grid(row=0, column=0, padx=10, pady=5)
Label(fr_1, text="Password  :").grid(row=1, column=0, padx=10, pady=5)
Entry(fr_1, textvariable=ent_1).grid(row=0, column=1, padx=10, pady=5)
Entry(fr_1, textvariable=ent_2, show="*").grid(row=1, column=1, padx=10, pady=5)
Label(fr_1, textvariable=lab).grid(row=2, column=0, columnspan=2)
Button(fr_2, text="Login", command=fun_login).grid(row=0, column=0, padx=10, pady=5)
Button(fr_2, text="Sign in", command=fun_signin).grid(row=0, column=1, padx=10, pady=5)
fr_1.pack()
fr_2.pack()

win_1.mainloop()

if open_win2 == 1:
    win_2=Tk()
    win_2.title('Sign a user')
    ent_1=StringVar()
    ent_2=StringVar()
    lab=StringVar()
    Label(win_2, text="User name :").grid(row=0, column=0, padx=10, pady=5)
    Label(win_2, text="Password  :").grid(row=1, column=0, padx=10, pady=5)
    Entry(win_2, textvariable=ent_1).grid(row=0, column=1, padx=10, pady=5)
    Entry(win_2, textvariable=ent_2).grid(row=1, column=1, padx=10, pady=5)
    Label(win_2, textvariable=lab).grid(row=2, column=0, columnspan=2)
    Button(win_2, text="OK", command=add_user).grid(row=3, column=0, columnspan=2)
    win_2.mainloop()

