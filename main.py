# import module
import time
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime
import win32api
import tkinter as tk
import asyncio

global txt_edit
SLEEPTIME = 120  # seconds
server = "https://refactor.jp/chivalry/?serverId=1486941"

def checkserver():
    global players

    while True:
        try:
            htmldata = getdata(server)
            soup = BeautifulSoup(htmldata, 'html.parser')
            for data in soup.find_all("tt"):
                players = data.get_text()[1:3]

            if players[0:1] != "0":
                # playsound('audio.mp3', False)
                print(players)
                txt_edit.insert(tk.END, players + '\n')
                return
                # win32api.MessageBox(0, players+' Players found', 'Result', 0x00001000)
            else:
                print(gettime(), "Nobody is playing on this server")
                time.sleep(SLEEPTIME)
                continue
            # To handle exceptions
        except:
            print("Internet disconnected? Server offline?")
            time.sleep(SLEEPTIME)
            checkserver()


def gettime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text


window = tk.Tk()
window.title("Check Chiv Servers")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Run Search", command=checkserver)
btn_save = tk.Button(fr_buttons, text="Change Server")

window.rowconfigure(0, minsize=500, weight=1)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()

checkserver()
