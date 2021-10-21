# import module
import time
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime
import win32api

SLEEPTIME = 120 #seconds

def checkserver():
    global players
    while True:
        try:
            htmldata = getdata("https://refactor.jp/chivalry/?serverId=1495246")
            soup = BeautifulSoup(htmldata, 'html.parser')
            for data in soup.find_all("tt"):
                players = data.get_text()[1:3]

            if players[0:1] != "0":
                playsound('audio.mp3', False)
                win32api.MessageBox(0, players+' Players found', 'Result', 0x00001000)
                userinput = input(
                    gettime() + " " + players + "players found! Please ENTER to stop searching or other key to search "
                                                "again: ")
                if len(userinput) == 0:
                    print("Done! Have fun playing")
                    break
                else:
                    continue
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


checkserver()
