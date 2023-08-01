# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 528f7bcb05d05e23a99d5c68ec9a1296
# Original link  : https://github.com/cebonganyut/revipnew
# Datetime       : 2023-08-02 00:56:02.992755
# Source size    : 4.6 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>

import requests
import re
import os.path
import string
import os
import sys
import time
from platform import system
from urllib import request
import warnings
from concurrent.futures import ThreadPoolExecutor
from importlib import reload
from colorama import init, Fore, Style
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
from licensing.models import *
from licensing.methods import Key, Helpers


RSAPubKey = "<RSAKeyValue><Modulus>tRaUFGCINM5rAFdtNo8Y1JKPCpYMmcBIQ2RQgjIBcx8NsRuNN3op/Vvxo/miq20eX9rsLKYIRgwJo+ioKB6tFj2N68OwhAPIfXq2Zoz/egRYQzOm+lCO6qtVR1rq6UvsYTKC3CJqq/I97SQah9kBGHqhkTcaTew9Hz24tsNm6WBKEDYKLlvSjdmFlvQpQRsaLrKxJTfCBdbi/gIxNclBthqOJ8DqX8a2ekIMEfR39fm69vVhPTINQJsQ2ouB0PXnxDA5FWEHRDCycaQTKV5gewVS7uRdcBI8e8nUTV/e3jCwkhbVTZmBfyj6cwv3Zm4A8pP+gdRiqmhlHvoMuJlJXw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"# ENTER RSAKEY
auth = "WyI1NTQxMDA2OCIsInNXVElpSTA1UDZMOG5ZM1RkZUlHeUtxdlJLeEVEMm5IdlFyMTduR1kiXQ==" ## AUTHKEY WITH ACTIVATE !
def Authkey():
    key = str(input(" Enter Auth Key :"))
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id=21078, \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] is None or not Helpers.IsOnRightMachine(result[0]):
        # An error occurred or the key is invalid or it cannot be activated
        # (e.g., the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
        sys.exit(1)  # Terminate the program with exit code 1 (indicating an error)
    else:
        # Everything went fine if we are here!
        print("The license is valid!")


# Call the Authkey() function to execute the license validation process
Authkey()
init(autoreset=True)
#try:
#	os.mkdir('Result') #createfolder
#	os.getcwd()
#except:
#	pass

reload(sys)
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

good=[]
bad=[]
failed =[]
GOOD = 0
BAD = 0
FAILED = 0

os.system("title " + "[+] GOOD:  {} , [-]BAD : {}  , [!]FAILED : {}  ".format(GOOD, BAD, FAILED))


banner = """
   {}____                                 ___ ____  {}
   {}|  _ \ _____   _____ _ __ ___  ___  |_ _|  _ \ {}
   {}| |_) / _ \ \ / / _ \ '__/ __|/ _ \  | || |_) |{}
   {}|  _ <  __/\ V /INSANCLAN13_/ |  \_\ | ||   __/{}  
   {}|_| \_\___| \_/ \___|_|  |___/\___| |___|_|    {}
   


""".format(r, c,c, c, g, g, c, g, g, c, c, c, r)
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def reverseip(i):
	global GOOD, BAD, FAILED
	try:
		grab = requests.get('https://rapiddns.io/s/'+i+'?full=1&down=1#result/', headers=headers, timeout=30).text
		if '<th scope="row ">' in grab:
			res = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', grab)
			print('{}[+] {}Reverse {}{} {}[{} {} {}DOMAINS]{}'.format(g, c, y, i, g, r, len(str(res)), g, o))
			for domain in res:
				domainku = domain.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
				open('Domains.txt', "a+").write(str(domainku)+'\n')
				good.append(i)
				GOOD += 1
				
		else:
			print('{}[-] {}Reverse {}{} {}[{} NO DOMAIN {}]{}'.format(r, c, y, i, g, r, g, r, o))
			bad.append(i)
			BAD += 1
	except KeyboardInterrupt:
		print('{}[-] {}Reverse {}{} {}[{} API FAILED OR WRONG {}]{}'.format(r, c, y, i, g, r, g, r, o))
		failed.append(i)
		FAILED += 1
		time.sleep(0.5)
		sys.exit()

def main():
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(banner)
		lists = input('\n{}[+] {}Website List{} > {}'.format(c, g, o, g).strip())
		power = int(input('{}[+] {}Thread{} > {}'.format(c, g, o,g, g)))
		print('')

		def runner():
			threads = []
			domainku = lists.replace('"', '')
			process = open(domainku, 'r').read().splitlines()
			with ThreadPoolExecutor(max_workers=power) as thread:
				[threads.append(thread.submit(reverseip, i)) for i in process]

		runner()
		print("\n\n{}[+] TOTAL GOODS {}:{}[{}{}{}]{}".format(g, o, g, o, str(len(good)), g, o))
		print("{}[-] TOTAL BADS {}:{}[{}{}{}]{}".format(c, o, c, o, str(len(bad)), r, o))
		print("{}[!] TOTAL FAILED {}:{}[{}{}{}]{}".format(r, o, r, o, str(len(failed)), r, o))
	except Exception as e:
		print('{}[!] {}Incorrect'.format(c, r))
		time.sleep(0.5)

if __name__ == '__main__':
	main()

