# import module
import webbrowser
from email.policy import default
import os
import sys
import time
from tkinter import *
from tkinter.constants import N
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from turtle import bgcolor, title, width
import winsound
from playsound import playsound
from winsound import PlaySound
import requests
from bs4 import BeautifulSoup

from datetime import datetime
import tkinter as tk
import multiprocessing

server = "https://refactor.jp/chivalry/?serverId="
searching = True

name = "Sandclusterfck 1.X in Finland"
file = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__))),'audio.mp3')


def check_players():
    global players
    server_id = e.get()
    htmldata = get_data(server+server_id)
    soup = BeautifulSoup(htmldata, 'html.parser')
    get_server_name(soup)
    for data in soup.find_all("tt"):
        players = data.get_text()[1:3]
        if players[1:2] == "/":
            players = players[0:1]
    return int(players)


def get_server_name(soup):
    global name
    for data in soup.find_all("h2"):        
        name = data.get_text()


def restart_server():
    global searching
    searching = True
    txt_edit.delete(1.0, END)
    check_server()


def check_server():
    if searching:
        update()

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


# link for extract html data
def get_data(url):
    r = requests.get(url)
    return r.text


def stop():
    winsound.PlaySound(None, winsound.SND_FILENAME)
    global searching
    searching = False
    window.title("Check Chiv Server: " + e.get())
    btn_runstop.config(text="Run Search", command=restart_server)
    txt_edit.insert(tk.END, get_time() + " " + "Stopped search \n")
    txt_edit.see(tk.END)

#default winsounds 
def playsound():    
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC + winsound.SND_LOOP)


def update():
    sleeptime = e_minutes.get()    
    btn_runstop.config(text="Stop", command=stop)
    playercheck = check_players()
    if playercheck > 1:
        txt_edit.insert(tk.END, get_time() + " " + players + " players online\n")
        playsound()
    elif playercheck == 1:
        txt_edit.insert(tk.END, get_time() + " " + players + " player online\n")
        playsound()
    else:
        txt_edit.insert(tk.END, get_time() + " Nobody is playing on this server" + "\n")    
    window.title("Searching: " + e.get() + " " + name)
    txt_edit.see(tk.END) #keep scolling to END in window
    window.after((int(sleeptime)*60000), check_server)  # run  again after xxx ms


def showinfo():    
    global server_id
    global searching
    server_id = askstring('serverId', 'Change Id here')
    if server_id:
        window.title("Check Chiv Server: " + server_id)
    stop()
    searching = True
    check_server()

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


window = tk.Tk()


window.geometry("370x230")
#window.configure(bg = "black")

scrollbar = tk.Scrollbar(window)
label = tk.Label(window, text="min(s)")
txt_edit = tk.Text(window, height=10, width=45)
fr_buttons = tk.Frame(window)
btn_runstop = tk.Button(fr_buttons, text="Run Search", command=check_server)
e = Entry(fr_buttons, justify='center', width=11)  
e.insert(END, '1495246')
e_minutes = Entry(window, justify='center', width=3)  
e_minutes.insert(END, 1)
window.title("Check Chiv Server: " + e.get())

lbl = tk.Label(window, text=r"https://refactor.jp/chivalry/?country=CONTINENT_EU", fg="grey", cursor="hand2")
lbl.grid(row=2, column=0)
lbl.bind("<Button-1>", callback)

window.columnconfigure(0, weight=1)
fr_buttons.grid(row=0, column=0, padx=10, pady=5, sticky=E)
e.grid(row=0, column=0, padx=5)
btn_runstop.grid(row=0, column=1, padx=5, pady=5)
e_minutes.grid(row= 0, column=0, padx=45, sticky=W)
txt_edit.grid(row=1, column=0, padx=10, sticky=W)
scrollbar.grid(row=1, column=1, rowspan=1)
label.grid(row=0, column=0, sticky=W)

txt_edit.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_edit.yview)
check_server()

window.mainloop()


