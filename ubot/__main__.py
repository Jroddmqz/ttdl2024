import time
import requests
from .config import Config
from .core import Core

api = "https://api.telegram.org/bot" + Config.TokenBot
update_id = 0
print("[+] Bot is actived !")
print("[+] press control + c to exit !")
res = requests.get(f"{api}/getme")
bot_name = res.json()['result']['first_name']
print(f"[+] bot name : {bot_name}")
print('~' * 40)
while True:
    try:
        req = requests.get(f"{api}/getupdates", params={"offset": update_id}).json()
        print(req)
        if len(req['result']) == 0:
            continue

        update = req["result"][0]
        print(update)
        try:
            x = update["message"]["chat"]["type"]
            Core(update)
        except:
            continue


        update_id = update['update_id'] + 1
        print("~" * 40)
    except ConnectionError:
        print('- connection error!,try again after 5 seconds !')
        time.sleep(5)
        continue
    except KeyboardInterrupt:
        exit()
