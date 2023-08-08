# <comment-start>
# Decompiled by Rizemary (BlackZoneCode)
# --------------------------------------
# File type      : Python File
# File hash (md5): 4cdedc1afcf664cb2303485596823d07
# Original link  : https://github.com/SkajpCZ/PyObfuscator
# Datetime       : 2023-08-08 16:17:03.112242
# Source size    : 7.8 KB
# Telegram       : @BZCTeam @Rizemary
# --------------------------------------
# <comment-end>

import os, time


def Obs():
    import random, json, string, base64, codecs

    class Obfuscator:
        def __init__(self, code):
            self.code = code
            self.__obfuscate()

        def __xorED(self, text, key=None):
            newstring = ""
            if key is None:
                key = "".join(
                    random.choices(
                        string.digits + string.ascii_letters, k=random.randint(4, 8)
                    )
                )
            if not key[0] == " ":
                key = " " + key
            for i in range(len(text)):
                newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
            return (newstring, key)

        def __encodestring(self, string):
            newstring = ""
            for i in string:
                if random.choice([True, False]):
                    newstring += "\\x" + codecs.encode(i.encode(), "hex").decode()
                else:
                    newstring += "\\" + oct(ord(i))[2:]
            return newstring

        def __obfuscate(self):
            xorcod = self.__xorED(self.code)
            self.code = xorcod[0]
            encoded_code = base64.b64encode(
                codecs.encode(codecs.encode(self.code.encode(), "bz2"), "uu")
            ).decode()
            encoded_code = [
                encoded_code[i : i + int(len(encoded_code) / 4)]
                for i in range(0, len(encoded_code), int(len(encoded_code) / 4))
            ]
            new_encoded_code = []
            new_encoded_code.append(
                codecs.encode(encoded_code[0].encode(), "uu").decode() + "u"
            )
            new_encoded_code.append(codecs.encode(encoded_code[1], "rot13") + "r")
            new_encoded_code.append(
                codecs.encode(encoded_code[2].encode(), "hex").decode() + "h"
            )
            new_encoded_code.append(
                base64.b85encode(
                    codecs.encode(encoded_code[3].encode(), "hex")
                ).decode()
                + "x"
            )
            self.code = f"""
_____=eval("{self.__encodestring('eval')}");_______=_____("{self.__encodestring('compile')}");______,____=_____(_______("{self.__encodestring("__import__('base64')")}","",_____.__name__)),_____(_______("{self.__encodestring("__import__('codecs')")}","",_____.__name__));____________________=_____("'{self.__encodestring(xorcod[True])}'");________,_________,__________,___________=_____(_______("{self.__encodestring('exec')}","",_____.__name__)),_____(_______("{self.__encodestring('str.encode')}","",_____.__name__)),_____(_______("{self.__encodestring('isinstance')}","",_____.__name__)),_____(_______("{self.__encodestring('bytes')}","",_____.__name__))
def ___________________(__________, ___________):
    __________=__________.decode()
    _________=""
    if not ___________[False]=="{self.__encodestring(' ')}":
        ___________="{self.__encodestring(' ')}"+___________
    for _ in range(_____("{self.__encodestring('len(__________)')}")):
        _________+=_____("{self.__encodestring('chr(ord(__________[_])^ord(___________[(len(___________) - True*2) + True]))')}")
    return (_________,___________)
def ____________(_____________):
    if(_____________[-True]!=_____(_______("'{self.__encodestring('c________________6s5________________6ardv8')}'[-True*4]","",_____.__name__))):_____________ = _________(_____________)
    if not(__________(_____________, ___________)):_____________ = _____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('rot13')}')","",_____.__name__))
    else:
        if(_____________[-True]==_____(_______("b'{self.__encodestring('f5sfsdfauf85')}'[-True*4]","", _____.__name__))):
            _____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('uu')}')","",_____.__name__))
        elif (_____________[-True] ==_____(_______("b'{self.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _____.__name__))):_____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{self.__encodestring('hex')}')","",_____.__name__))
        else:_____________=_____(_______("{self.__encodestring('______.b85decode(_____________[:-True])')}","",_____.__name__));_____________=_____(_______("{self.__encodestring('____.decode(_____________')}, '{self.__encodestring('hex')}')","",_____.__name__))
        _____________=_____(_______("{self.__encodestring('___________.decode(_____________)')}","",_____.__name__))
    return _____________
_________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_____.__name__));________________ = _____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_____.__name__));__________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_____.__name__));______________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_____.__name__));_______________=_____(_______("{self.__encodestring('str.join')}('', {self.__encodestring('[____________(x) for x in [______________,________________,__________________,_________________]]')})","", _____.__name__));________(___________________(____.decode(____.decode(______.b64decode(_________(_______________)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),____________________)[_____("{self.__encodestring('False')}")])\n{imports}"""

    def mainOBS():
        save_file = file_name.split("/")
        save_file.reverse()
        files = f"obs_{save_file[0]}"
        with open(file_name, encoding="utf-8") as file:
            CODE = file.read()
        obfuscator = Obfuscator(CODE)
        with open(files, "w", encoding="utf-8") as output_file:
            output_file.write(
                """
########### obfuscation | by Skajpik#3232 ############
#                                                    #
# Made by: Skajp                                     #
# Github: https://github.com/SkajpCZ/PyObfuscator    #
#                                                    #
######################################################
            """
            )
            output_file.write(obfuscator.code)
        print("\033[1;32m" + "\n Obsfucated")
        time.sleep(5)
        quit()

    file_name = input(
        "\t\033[1;93m"
        + "\n File For Obsfucation (Drag it in)"
        + "\033[1;90m"
        + " > "
        + "\033[0;37m"
        + f""
    )
    file_name = file_name.replace("\\", "/").strip('"')
    if ".py" in file_name:
        pass
    else:
        print("\n\033[1;31m Only for python scripts")
        time.sleep(5)
        quit()
    bruh = ""
    try:
        file_read = open(file_name, "r")
        text = "import "
        lines = file_read.readlines()
        new_list = []
        idx = 0
        for line in lines:
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        file_read.close()
        lineLen = len(new_list)
        for i in range(lineLen):
            if "(" or "." or ")" or "'" in new_list[i].strip():
                pass
            else:
                bruh += new_list[i].strip() + ";"
    except:
        print("\nThe file doesn't exist!")

    l = len(bruh)
    imports = bruh[: l - 1]
    mainOBS()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

print(
    f"""\033[1;36m
        ____        ____  __        
       / __ \__  __/ __ \/ /_  _____
      / /_/ / / / / / / / __ \/ ___/
     / ____/ /_/ / /_/ / /_/ (__  ) 
    /_/    \__, /\____/_.___/____/  
          /____/                   \033[1;37mby \033[1;90mSkajp
                                   \033[1;37mVersion: \033[1;90m2
"""
)


Obs()
