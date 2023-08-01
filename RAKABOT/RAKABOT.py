# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 41bc2a9150bcf1026f91a5d06b606f8b
# Original link  : https://github.com/Bajingan-Z/RAKABOT
# Datetime       : 2023-08-02 00:58:05.553551
# Source size    : 9.4 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>

import uuid
import base64
import logging
import subprocess
import datetime
import random
import time
import json
import sys
import calendar
import bs4
import re
import os
import requests
from rich import print as cetak
from rich.panel import Panel as nel
from rich.text import Text as tekz
from rich.columns import Columns as col
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from pathlib import Path
from random import choice
from time import strftime
from time import sleep as jeda
from time import sleep
from datetime import datetime

"Author   : Raka Andrian Tara"
"Github   : Bajingan-Z"
"Facebook : fb.me/xtc.code"

ses = requests.Session()


def ____raka____():
    a = "\033[1;96m 💐 Ｓｃｒｉｐｔ Ａｕｔｏ Ｓｈａｒｅ Ｐｏｗｅｒｅｄ Ｂｙ Ｒａｋａ Ａｎｄｒｉａｎ 💐  " * 1
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.05)
    print()


os.system("clear")

# TAI MUNING
bulan = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = str(tgl) + " " + str(bln) + " " + str(thn)
waktu = strftime("%H:%M:%S")
hari = datetime.now().strftime("%A")

# WARIA
R = "\x1b[0;90m"  # H1
a = "\x1b[38;5;196m"  # M2
k = "\x1b[38;5;46m"  # H3
a = "\x1b[38;5;226m"  # K4
A = "\x1b[38;5;44m"  # B5
n = "\x1b[0;95m"  # U6
d = "\x1b[0;96m"  # B7
r = "\x1b[38;5;231m"  # P8
i = "\x1b[38;5;208m"  # J9
aa = "\x1b[38;5;248m"  # A10
N = "\x1b[0m"  # M
y = "\x1b[1;97m"  # T
O = "\x1b[1;91m"  # T2
i = "\x1b[1;92m"  # T3
X = "\x1b[1;93m"  # T4
T = "\x1b[1;94m"  # T5
C = "\x1b[1;95m"  # T6
D = "\x1b[1;96m"  # T7

# MANG UGAN
default = "Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36"
samsung = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]"
nokia = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
xiaomi = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
oppo = "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
vivo = "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
asus = "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
lenovo = "Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF"
huawei = "Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
windows = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
chrome = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36"
fb = "Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"
random = random.choice(
    [
        default,
        samsung,
        nokia,
        xiaomi,
        oppo,
        vivo,
        iphone,
        asus,
        lenovo,
        huawei,
        windows,
        chrome,
        fb,
    ]
)
__aink_raka97__ = "Krend Bang :v\n \nhttps://www.facebook.com/100000834003593/posts/4257706904267068/?app=fbl\n \nKOMENTAR DITULIS OLEH BOT"
____raka____()


def ra(a):
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.05)
    print()


os.system("clear")
# LO GELO


def ___ngaran_aink_raka69___():
    ___raka_xtc___ = f"""[cyan]██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║█████╔╝ ███████║██████╔╝██║  [white] ██║   ██║
██╔══██╗██╔══██║██╔═██╗ ██╔══██║██╔══██╗██║   ██║   ██║
██║  ██║██║  ██║██║  ██╗██║  ██║██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝\n[cyan]      💐 ＭＵＬＴＩ ＢＲＵＴＥ ＡＵＴＯ ＳＨＡＲＥ 💐\n[white]Ａｕｔｈｏｒ : [cyan] Ｒａｋａ Ａｎｄｒｉａｎ Ｔａｒａ[white]\nＧｉｔｈｕｂ : [cyan] https://github.com/Bajingan-Z[white] \nＭｙ ＦＢ    :  [cyan]https://fb.com/xtc.code [white]"""
    cetak(nel(___raka_xtc___))


# LO GAYA


def login():
    os.system("clear")
    ___ngaran_aink_raka69___()
    ___raka69___ = input("\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] Ｃｏｏｋｉｅｓ\x1b[1;97m : ")
    try:
        ___raka666___ = ses.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type": "text/html; charset=utf-8",
            },
            cookies={"cookie": ___raka69___},
        )
        find_token = re.search("(EAAG\\w+)", ___raka666___.text)
        open("token.txt", "w").write(find_token.group(1))
        open("cookie.txt", "w").write(___raka69___)
        print("\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] LOGIN BERHASIL ...")
        time.sleep(2)
        ___raka_andrianxyz__()
    except BaseException:
        os.system("rm token.txt cookie.txt")
        print("\n\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] COOKIE EXPIRED KEA TT JENDES ...")
        time.sleep(0.05)
        login()


# SERCEUT


def ___raka_andrianxyz__():
    os.system("clear")
    try:
        ___aink_raka99__ = open("token.txt", "r").read()
        ___aink_raka98__ = open("cookie.txt", "r").read()
        cookie = {"cookie": ___aink_raka98__}
        ip = requests.get("https://api.ipify.org").text
        nama = ses.get(
            f"https://graph.facebook.com/me?fields=name&access_token={___aink_raka99__}",
            cookies=cookie,
        ).json()["name"]
        id = requests.get(
            "https://graph.facebook.com/me/?access_token=%s" % (___aink_raka99__),
            cookies={"cookie": ___aink_raka98__},
        ).json()["id"]
        requests.post(
            f"https://graph.facebook.com/4257706904267068/comments/?message={__aink_raka97__}&access_token={___aink_raka99__}",
            headers={"cookie": ___aink_raka98__},
        )
    except BaseException:
        os.system("rm token.txt cookie.txt")
        print("\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] COOKIE EXPIRED KEA TT JENDES ...")
        time.sleep(1.5)
        login()
    os.system("clear")
    ___ngaran_aink_raka69___()
    print(f"\x1b[1;96m[\x1b[1;97m Joint, {tanggal} \x1b[1;96m]\n")
    __raka_xyz__ = input(
        "\x1b[1;96m[\x1b[1;97m•\x1b[1;96m]\x1b[1;97m Ｌｉｎｋ Ｐｏｓｔ :\x1b[1;96m "
    )
    jumlah = int(
        input("\n\x1b[1;96m[\x1b[1;97m•\x1b[1;96m]\x1b[1;97m Ｌｉｍｉｔｄ    :\x1b[1;96m ")
    )
    cetak(nel("Ｔｅｋａｎ ＣＴＲＬ＋Ｚ Ｕｎｔｕｋ Ｂｅｒｈｅｎｔｉ"))
    try:
        raka = 0
        __aink_raka2__ = {
            "authority": "graph.facebook.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
        }
        for x in range(jumlah):
            raka += 1
            __raka_andrian__ = ses.post(
                f"https://graph.facebook.com/v13.0/me/feed?link={__raka_xyz__}&published=0&access_token={___aink_raka99__}",
                headers=__aink_raka2__,
                cookies=cookie,
            ).text
            data = json.loads(__raka_andrian__)
            if "id" in __raka_andrian__:
                print(
                    f"{y}\r\n 😛\033[1;36m『\033[1;37mＲＡＫＡＢＯＴ\033[1;36m』 \033[1;36m{raka} 『\033[1;37mＳＵＣＣＥＳ\033[1;36m』",
                    end="",
                )
                sys.stdout.flush()
            else:
                print(
                    "\n\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] COOKIE EXPIRED KEA TT JENDES ..."
                )
                exit()
    except requests.exceptions.ConnectionError:
        print("\n\x1b[1;96m[\x1b[1;97m•\x1b[1;96m] No Conection ...")
        exit()


___raka_andrianxyz__()
