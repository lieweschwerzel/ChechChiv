# import module
import time
import requests
from bs4 import BeautifulSoup
from playsound import playsound



# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text

while True:

        htmldata = getdata("https://refactor.jp/chivalry/?serverId=1491190")
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        onlinePlayers = soup.find_all("td")
        if len(onlinePlayers) > 0:
            print(str(len(onlinePlayers)/3) + " players")
            playsound('audio.mp3', False)
            var = input("Please ENTER to stop searching or other key to continue: ")
            if len(var) == 0:
                print("STOPPING")
                break
            else:
                time.sleep(30)
                continue
        else:
            print("Nobody is playing on this server")
            time.sleep(60)
            continue
        # To handle exceptions


