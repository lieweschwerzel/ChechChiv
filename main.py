# import module
from cgitb import text
import webbrowser
from email.policy import default
import os
import sys
from tkinter import *
import tkinter as tk
import winsound
from playsound import playsound
from winsound import PlaySound
import requests
from bs4 import BeautifulSoup
from datetime import datetime


server = "https://refactor.jp/chivalry/?serverId="
Timer_id = None #timer voor window.after(schedule)
DEFAULT_SERVER_ID = '1495246'
player_names = []
name = "Sandclusterfck 1.X in Finland"
#file = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__))),'audio.mp3')


def check_players():
    global players
    global player_names
    global name
    #get serverId from input entry
    server_id = entry_id.get()
    # link for extract html data
    htmldata = requests.get(server+server_id).text
    soup = BeautifulSoup(htmldata, 'html.parser')


    # #get servername
    for data in soup.find_all("h2"):        
        name = data.get_text()
   
    #get amount players
    for data in soup.find_all("tt"):
        players = data.get_text()[1:3]
        if players[1:2] == "/":
            players = players[0:1]

    
    raw_player_names = soup.find_all("td")
    # i = 0
    # while i < (len(raw_player_names)-1):
    #     player_names.append(raw_player_names[i])
    #     i+3
    
    print(len(raw_player_names))

       
    return int(players)


def run_search():
    global Timer_id
    
    sleeptime = e_minutes.get()        
    btn_runstop.config(text="Stop", command=stop_search)
    playercheck = check_players()
    if playercheck > 1:
        txt_main.insert(tk.END, get_time() + "  " + players + " players online\n")
        playsound()
    elif playercheck == 1:
        txt_main.insert(tk.END, get_time() + "  " + players + " player online\n")
        playsound()
    else:
        txt_main.insert(tk.END, get_time() + "  Nobody is playing on this server" + "\n")    
    window.title("Searching: " + entry_id.get() + " " + name)
    txt_main.see(tk.END) #keep scolling to END in window    
    
    Timer_id = window.after(int(float(sleeptime)*60000), run_search)  # run  again after xxx ms


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def stop_search():
    if Timer_id:
        window.after_cancel(Timer_id) # cancel the scheduled task
    winsound.PlaySound(None, winsound.SND_FILENAME)
   # window.title("Check Chiv Server: " + entry_id.get())
    btn_runstop.config(text="Run Search", command=reset_search)
    txt_main.insert(tk.END, get_time() + "  Stopped search \n")
    txt_main.see(tk.END)


def reset_search():
    txt_main.delete(1.0, END)
    run_search()


#default winsounds 
def playsound():    
    if cb_entry.get() == 1:
        winsound.PlaySound('SystemHand', winsound.SND_ASYNC + winsound.SND_LOOP)

#open link to website
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

#checkbox alarm
def isChecked():
    if cb_entry.get() == 0:
        winsound.PlaySound(None, winsound.SND_FILENAME)



#####################Front TK ####################

window = tk.Tk()

window.geometry("370x230")
window.minsize(370,230)
window.maxsize(370,230)
window.resizable(0,0)
#window.configure(bg = "black")

scrollbar = tk.Scrollbar(window)
label = tk.Label(window, text="min(s)")
txt_main = tk.Text(window, height=10, width=45)
fr_buttons = tk.Frame(window)
btn_runstop = tk.Button(fr_buttons, width=10, text="Run Search", command=run_search)
entry_id = Entry(fr_buttons, justify='center', width=11)  
entry_id.insert(END, DEFAULT_SERVER_ID)
e_minutes = Entry(window, justify='center', width=3)  
e_minutes.insert(END, 1)
window.title("Check Chiv Server: " + entry_id.get())

cb_entry = IntVar()
checkbox = tk.Checkbutton(window, text="Alarm", variable=cb_entry, onvalue=1, offvalue=0, command=isChecked)
checkbox.select()

lbl = tk.Label(window, text=r"https://refactor.jp/chivalry/?country=CONTINENT_EU", fg="grey", cursor="hand2")
lbl.grid(row=2, column=0)
lbl.bind("<Button-1>", callback)

window.columnconfigure(0, weight=1)
fr_buttons.grid(row=0, column=0, padx=10, pady=5, sticky=E)
entry_id.grid(row=0, column=0, padx=5)
btn_runstop.grid(row=0, column=1, padx=(5,0), pady=5)
label.grid(row=0, column=0, padx=10, sticky=W)
e_minutes.grid(row= 0, column=0, padx=50, sticky=W)
checkbox.grid(row=0, column=0, padx=(100,0), sticky=W)
txt_main.grid(row=1, column=0, padx=(10,0), sticky=W)
scrollbar.grid(row=1, column=2, rowspan=2, sticky=NSEW)

txt_main.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_main.yview)

run_search()

window.mainloop()


