#Made by Razi Falah
#Copyright (C) 2022 razifalah.com
#https://razifalah.com
#According to the applied license: LICENSE GNU General Public License v3.0
#You do not have the right to republish sell or edit this project, use it only for private use or educational purposes


import tkinter as tk
from tkinter.constants import CENTER, COMMAND, LEFT, TOP, TRUE
import os

window = tk.Tk()
window.title("Login to cyberfriend")


## you can connect to database instad of dict
users = {
    "razifalah" : {
        "password": "azs12azs"
    }
}

connection_check = "Connection is up and running"

def submit():
        user = username_ent.get()
        password = password_ent.get()
        if user in users:
           if users[user]["password"] == password:
               success = tk.Label(
                   text="Login success",
                   bg="green",
                   master=login_frm
               )
               success.pack()
               mark = open("logs.txt", "a")
               mark.write(f"[WARNING](USER)_Loggedin_=def-submit+l37flogin.py!!action==login_success||{password} and {user}||\n")
               mark.close()
               os.system('python3 app.py')
               exit()
           else:
                mark = open("logs.txt", "a")
                mark.write(f"[WARNING](USER)_Loggedin_=def-submit+l43flogin.py!!action==login_failed||{password} and {user}||\n")
                mark.close()
                wrong = tk.Label(
                    text="Login failed",
                    bg="red",
                    master=login_frm
                )
                wrong.pack()
        elif user == "exit":
            mark = open("logs.txt", "a")
            mark.write(f"[WARNING](USER)_exit_=def-submit+l53flogin.py!!action==exit\n")
            mark.close()
            exit()
        else:
            mark = open("logs.txt", "a")
            mark.write(f"[WARNING](USER)_Loggedin_=def-submit+l58flogin.py!!action==login_failed||{password} and {user}||\n")
            mark.close()
            unfound = tk.Label(
                text="Invaild username",
                bg="red",
                master=login_frm
            )
            unfound.pack()




login_frm = tk.Frame(
    master=window,
    bg="blue",
)
username_lbl = tk.Label(
    text="Enter your name",
    master=login_frm,
    bg="blue",
    fg="white"
)
username_lbl.pack()
username_ent = tk.Entry(
    width=40,
    master=login_frm,
)
username_ent.pack()
password_lbl = tk.Label(
    text="Enter your password",
    master=login_frm,
    bg="blue",
    fg="white"
)
password_lbl.pack()
password_ent = tk.Entry(
    width=40,
    master=login_frm,
)
password_ent.pack()
empty_lbl = tk.Label(
    text=" ",
    master=login_frm,
    bg="blue",
)
empty_lbl.pack()
submit_btn = tk.Button(
    text="Log in",
    master=login_frm,
    command=submit
)
submit_btn.pack()


login_frm.pack(expand=True, fill=tk.BOTH)
window.attributes('-fullscreen', True)
window.mainloop()