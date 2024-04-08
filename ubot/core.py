import json
import os

from requests import *
from .tiktok_downloader import downloader
from datetime import datetime
from .telegram import send_message, send_video, delete_message


def get_time(tt):
    tt = datetime.fromtimestamp(tt)
    hour = str(tt.hour).zfill(2)
    minute = str(tt.minute).zfill(2)
    second = str(tt.second).zfill(2)
    day = str(tt.day).zfill(2)
    mon = str(tt.month).zfill(2)
    year = str(tt.year).zfill(4)

    return f"{year}-{mon}-{day} {hour}:{minute}:{second}"


def Core(data):
    try:
        video_name = "video.mp4"
        dl = downloader(video_name)
        user_id = None
        first_name = None
        text = None
        print(data)
        chat_type = data["message"]["chat"]["type"]
        print(chat_type)
        message_date = data['message']['date']
        message_id = data['message']['message_id']

        if 'first_name' in data['message']['chat'].keys():
            first_name = data["message"]["chat"]["first_name"]

        if 'id' in data['message']['chat'].keys():
            user_id = data['message']['chat']['id']

        if 'text' in data['message'].keys():
            text = data['message']['text']

        if chat_type != "private":
            send_message(user_id, "uwu r", message_id)
        # return

        rl_time = get_time(message_date)
        print(f'[+] time : {rl_time}')
        print(f'[+] from : {user_id} | {first_name}')
        print(f'[+] message : {text}')
        if text.startswith('/start'):
            msg = """Hola mi nombre es Klee, estaré encantada de ayudarte con lo que necesites, así que, si necesitas algo, tan solo pídelo!

Como usar el bot:
🇲🇽 : Envia enlace de tiktok

eg : https://vm.tiktok.com/ZMMHtWnyb/"""
            send_message(user_id, msg, message_id)
            return

        if "https://" in text and "tiktok.com" in text and \
                len(text.split()) == 1 and text.find("http") == 0:
            original_link = (text.split("?")[0] if text.find("?") >= 0 else text)
            msg = f"""
Estoy muy feliz de ayudarte!...
Por favor! No dudes en volver!
{original_link}

💥 @dodocodocobot 💥
"""

            # res = dl.tiktapio(text)
            # if res:
            #	print("[+] success download with tiktapio !")
            #	delete_message(user_id,message_id)
            #	send_video(user_id,video_name,msg)
            #	return

            res = dl.tiktapiocom(text)
            if res:
                print("[+] success download with tiktapiocom !")
                delete_message(user_id, message_id)
                send_video(user_id, video_name, msg)
                send_video(5401798077, video_name, msg)
                os.remove(video_name)
                return

            res = dl.tikmatecc(text)
            if res:
                print("[+] success download with tikmatecc !")
                delete_message(user_id, message_id)
                send_video(user_id, video_name, msg)
                send_video(5401798077, video_name, msg)
                os.remove(video_name)
                return

            res = dl.snaptikpro(text)
            if res:
                print("[+] success download with snaptikpro !")
                delete_message(user_id, message_id)
                send_video(user_id, video_name, msg)
                send_video(5401798077, video_name, msg)
                os.remove(video_name)
                return

            res = dl.musicaldown(text)
            if res:
                print("[+] success download with musicaldown !")
                delete_message(user_id, message_id)
                send_video(user_id, video_name, msg)
                send_video(5401798077, video_name, msg)
                os.remove(video_name)
                return

            msg = """🇺🇸 : failed to download the video, check the link and try again later !
🇲🇽 : fallo descargar el video, revisa tu enlace y reenvia !"""
            send_message(user_id, msg, message_id)
            return

        if text.startswith("/donation"):
            msg = """Visitame en @LatamGenshinImpact"""
            send_message(user_id, msg, message_id)
            return

    except KeyboardInterrupt as e:
        print(f"[x] {e}")
        open(".log", "a+", encoding="utf-8").write(str(data) + "\n")
        return
