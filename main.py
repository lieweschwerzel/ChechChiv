# import module
from asyncio import events
from email.mime import audio
import os
import sys
import time
import PySimpleGUI as sg

from tkinter import END
from tkinter.constants import N
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from winsound import PlaySound
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime


SLEEPTIME = 6000  # milliseconds
server_id = "1495246"
server = "https://refactor.jp/chivalry/?serverId="
searching = True
name = "Sandclusterfck 1.X in Finland"
file = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(
    os.path.dirname(__file__))), 'audio.mp3')

def check_players():
    global players
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
    stop()
    check_server()


def check_server():
    while searching:
        try:
            update()
            return
            # To handle exceptions
        except:
            return txt_edit.insert(tk.END, get_time() + " " + "Wrong ID or connection issues \n")


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


# link for extract html data
def get_data(url):
    r = requests.get(url)
    return r.text

def scan():
    while searching:
        try:
            update()
            print('3 sec')
            window.read(timeout=4000)      
            print("voorbij")  
            scan()
            return
            # To handle exceptions
        except:
            return print(get_time() + " " + "Wrong ID or connection issues \n")


def update():
    global searching
    update_players = check_players()
    print(update_players)    
    scan_button.Update('stop')
    window['-TEXT-'].update(get_time() + " " + str(update_players) +"\n", append=True)
    if event == 'stop':
        print("ASDSDAFSADFSAF") 
        searching = False

   # window['-TEXT-'].update("Players on this server: " +str(update_players))


def stop():
    global searching
    searching = False





scan_button = sg.Button('scan', bind_return_key=True)
text = sg.Multiline(size=(30, 15), autoscroll=True, key='-TEXT-')

left_col = [
    [scan_button]
]

right_col = [
    [text]
]

layout = [
    [
        left_col,
        sg.Frame(layout = right_col, title='', size = (250, 300)),
    ]
]

#create window
window = sg.Window("Chivalry Server", layout, margins=(10,10))

#create event loop
while True:
    event, values = window.read()

    #close when user closes window or presses OK
    if event == sg.WIN_CLOSED:        
        break
    if event == 'scan':
        scan()
  
    
window.close()




    # window.title("Check Chiv Server: " + server_id)
    # btn_open.config(text="Run Search", command=restart_server)
    # txt_edit.insert(tk.END, get_time() + " " + "Stopped search \n")
    # txt_edit.see(tk.END)





   # window.title("Searching: " + server_id + " " + name)
    # btn_open.config(text="Stop", command=stop)
    # playercheck = check_players()
    # if playercheck > 1:
    #     txt_edit.insert(tk.END, get_time() + " " +
    #                     players + " players online\n")
    #     playsound(file, False)
    # elif playercheck == 1:
    #     txt_edit.insert(tk.END, get_time() + " " +
    #                     players + " player online\n")
    #     playsound(file, False)
    # else:
    #     txt_edit.insert(tk.END, get_time() +
    #                     " Nobody is playing on this server" + "\n")
    # txt_edit.see(tk.END)  # keep scolling to END in window
    # window.after(SLEEPTIME, check_server)  # run  again after xxx ms


# def showinfo():
#     global server_id
#     server_id = askstring('serverId', 'Change Id here')
#     if server_id:
#         window.title("Check Chiv Server: " + server_id)


# window = tk.Tk()
# window.title("Check Chiv Server: " + server_id)

# window.geometry("650x200")
# window.rowconfigure(0, minsize=10, weight=1)
# window.columnconfigure(1, minsize=100, weight=1)

# scrollbar = tk.Scrollbar(window)
# label = tk.Label(window)
# txt_edit = tk.Text(window)
# sec_edit = tk.Entry(window)
# fr_buttons = tk.Frame(window)
# btn_open = tk.Button(fr_buttons, text="Run Search", command=check_server)
# btn_save = tk.Button(fr_buttons, text="Change Server", command=showinfo)

# btn_open.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
# sec_edit.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
# fr_buttons.grid(row=0, column=1, sticky="ns")
# txt_edit.grid(row=0, column=2, sticky="nsew")
# scrollbar.grid(row=0, column=4, rowspan=2,  sticky="nsew")
# label.grid(row=2, column=2, sticky="nsew")

# txt_edit.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=txt_edit.yview)

# window.mainloop()
