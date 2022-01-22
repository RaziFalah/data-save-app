#Made by Razi Falah
#Copyright (C) 2022 razifalah.com
#https://razifalah.com
#According to the applied license: LICENSE GNU General Public License v3.0
#You do not have the right to republish sell or edit this project, use it only for private use or educational purposes


import tkinter as tk
from tkinter.constants import CENTER, COMMAND, LEFT, TOP, TRUE
import os

window = tk.Tk()
window.title("welcome to cyberfriend")





login_frm = tk.Frame(
    master=window,
    bg="blue",
)

msg_lbl = tk.Label(
    master=login_frm,
    text="Hello Razi, You are in!!",
    bg="white"
)



server1_lbl = tk.Label(
    master=login_frm,
    text="razifalah.com is oprating at successfuly",
    fg="blue",
    bg="green"
)

def wayout():
    mark = open("logs.txt", "a")
    mark.write("[WARNING](USER)_WAYOUT_=def-wayout+l48fapp.py!!action==success\n")
    mark.close()
    exit()

exit_btn = tk.Button(
    text="Exit",
    master=login_frm,
    bg="blue",
    command=wayout
)



exit_btn.pack()
msg_lbl.pack()
server1_lbl.pack()
login_frm.pack(expand=True, fill=tk.BOTH)
window.attributes('-fullscreen', True)
window.mainloop()