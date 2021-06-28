# import module
import time
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from datetime import datetime

SLEEPTIME = 58


def checkserver():
    global players
    while True:
        try:
            htmldata = getdata("https://refactor.jp/chivalry/?serverId=1491190")
            soup = BeautifulSoup(htmldata, 'html.parser')
            for data in soup.find_all("tt"):
                players = data.get_text()[1:3]

            if players[0:1] != "0":
                playsound('audio.mp3', False)
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
            print("Internet disconnected?")
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
