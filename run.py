#--------------- MODULE ---------------
import requests
import sys, os
import time
from asciimatics.screen import Screen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from time import sleep
from random import randint, choice
from pyfiglet import Figlet

#--------------- COLOR ---------------
# Warna dasar
X = "\033[0m" # Reset warna
B = "\033[1m" # Bold
I = "\033[3m" # Italic
U = "\033[4m" # Underline
S = "\033[9m" # Strikethrough
R = "\033[7m" # Reverse

# Warna teks
BK = "\033[30m" # Hitam
RD = "\033[31m" # Merah
GN = "\033[32m" # Hijau
YW = "\033[33m" # Kuning
BL = "\033[34m" # Biru
MAGENTA = "\033[35m" # Magenta
CYAN = "\033[36m" # Cyan
W = "\033[37m" # Putih

# Warna teks terang
GR = "\033[90m" # Abu-abu
LRD = "\033[91m" # Merah terang
LGN = "\033[92m" # Hijau terang
LYW = "\033[93m" # Kuning terang
LBL = "\033[94m" # Biru terang
LMAGENTA = "\033[95m" # Magenta terang
LCYAN = "\033[96m" # Cyan terang
Lw = "\033[97m" # Putih terang

# Warna background
BG_BLACK = "\033[40m" # Hitam
BG_RED = "\033[41m" # Merah
BG_GREEN = "\033[42m" # Hijau
BG_YELLOW = "\033[43m" # Kuning
BG_BLUE = "\033[44m"    # Biru
BG_MAGENTA = "\033[45m" # Magenta
BG_CYAN = "\033[46m" # Cyan
BG_WHITE = "\033[47m" # Putih

# Warna background terang
BG_GRAY = "\033[100m" # Abu-abu
BG_LRED = "\033[101m" # Merah terang
BG_LGREEN = "\033[102m" # Hijau terang
BG_LYELLOW = "\033[103m" # Kuning terang
BG_LBLUE = "\033[104m" # Biru terang
BG_LMAGENTA = "\033[105m" # Magenta terang
BG_LCYAN = "\033[106m" # Cyan terang
BG_LWHITE = "\033[107m" # Putih terang

def RGB(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

YELLOW_GOLD = RGB(255, 215, 0)
NEON_GREEN  = RGB(0, 255, 0)
SKY_BLUE    = RGB(0, 191, 255)
CYAN_BRIGHT = RGB(0, 255, 255)
PINK        = RGB(255, 0, 255)
HOT_PINK    = RGB(255, 105, 180)
DEEP_PINK   = RGB(255, 20, 147)
VIOLET      = RGB(138, 43, 226)
INDIGO      = RGB(75, 0, 130)

NameAdmin = "AdiyZd Coder >_"

#--------------- FLAG TEXT ---------------
fig = Figlet(font='slant')
Logo1 = fig.renderText("Login").splitlines()
logo2_under = fig.renderText("Finder").splitlines()

CLEANING = os.system('cls' if os.name == 'nt' else 'clear')

#--------------- LOGO ---------------

logoScript = []
for line in Logo1:
    logoScript.append(f"{YELLOW_GOLD}{line}{X}")
for line in logo2_under:
    logoScript.append(f"{CYAN_BRIGHT}{line}{X}") 
    
logoScript.append(f"{X}Welcome to Login Finder Script{X}")
logoScript.append(f"{LRD}Script by: {NameAdmin}{X}")




#--------------- WELCOME ---------------
def Wlecome(Ctext=logoScript, Thitungan=5,):
    #--------------- ANY Riverst ---------------
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(Thitungan, -1, -1):
        sys.stdout.write(f"\r {LGN}Loading: {X} {i}")
        sys.stdout.flush()
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    #--------------- CETAK LOGO ---------------
    jarak_kanan_kiri = Ctext
    jarak_atas_bawah = os.get_terminal_size().columns
    for line in jarak_kanan_kiri:
        print(line.center(jarak_atas_bawah))
    print("\n" + "=" * 76)

#--------------- URL Finder ---------------
def URLFinder(url,):
    try:
        hdrs = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # halaman yang ingin diakses
        response = requests.get(url, headers=hdrs, timeout=10)
        response.raise_for_status() # Memastikan tidak ada error pada request
        
        # mengecek link yang mungkin ada halaman login nya nih 
        login_page = [
            'login', 'register', 'sign-in', 'signup', 'auth', 'account', 'log-in', 'signin', 'user', 'member', 'access', 'auth', 'authenticate', 'login.php', 'login.html', 'login.jsp', 'login.asp', 'login.aspx'
            , 'login.cgi', 'login.php3', 'login.py', 'login.rb', 'login.pl', 'login.sh', 'login.bat', 'login.exe', 'login.jar', 'login.war', 'login.xml'
            , 'login.json', 'login.yaml', 'login.yml', 'login.txt', 'login.md', 'login.css', 'login.js', 'login.xml', 'login.svg', 'login.gif', 'login.png', 'login.jpg', 'login.jpeg'
            , 'login.ico', 'login.svgz', 'login.webp', 'login.avif', 'login.tiff', 'login.tif', 'login.bmp', 'login.psd', 'login.eps', 'login.ai'
            , 'login.indd', 'login.inx', 'login.idml', 'login.odg', 'login.odt', 'login.ods', 'login.odp', 'login.odg', 'login.odf', 'login.ott', 'login.ots', 'login.otp', 'login.odg'
            ]
        soup = BeautifulSoup(response.text, 'html.parser')
        
        login_links = []
        for linknya in soup.find_all('a', href=True):
            href = linknya['href'].lower()
            if any(keyword in href for keyword in login_page):
                login_links.append(urljoin(url, linknya['href']))
            
        if login_links:
            login_urls = login_links[0]
            login_paket = requests.get(login_urls, headers=hdrs, timeout=10)
            login_soup = BeautifulSoup(login_paket.text, 'html.parser')
            
            forms = login_soup.find_all('form')
            login_forms = []
            
            for form in forms:
                inputs = form.find_all('input')
                has_user = any(i.get('name', '').lower() in ['username', 'email', 'user'] for i in inputs)
                has_pass = any(i.get('type', '').lower() == 'password' for i in inputs)
                
                if has_user and has_pass:
                    login_forms.append({
                        'action' : form.get('action', ''),
                        'method' : form.get('method', 'get').upper(),
                        'inputs' : [{'name' : i.get('name'), 'type' : i.get('type')} for i in inputs]
                    })
                    
            return {
                'login_urls' : login_urls,
                'login_forms' : login_forms,
                'status' : 'login page ditemukan' if login_forms else 'point tidak ditemukan',
            }
            
        common_login_patch = [
            '/login', '/auth', '/register', '/account', '/user', '/member', '/access', '/auth', '/authenticate',
            '/signin', '/sign-in', '/signup', '/register', '/log-in', '/login.php', '/login.html',
            '/login.jsp', '/login.asp', '/login.aspx', '/login.cgi', '/login.php3', '/login.py',
            '/login.rb', '/login.pl', '/login.sh', '/login.bat', '/login.exe', '/login.jar',
            '/login.war', '/login.xml', '/login.json', '/login.yaml', '/login.yml', '/login.txt',
            '/login.md', '/login.css', '/login.js', '/login.svg', '/login.gif', '/login.png',
            '/login.jpg', '/login.jpeg', '/login.ico', '/login.svgz', '/login.webp', '/login.avif',
            '/login.tiff', '/login.tif', '/login.bmp', '/login.psd', '/login.eps', '/login.ai',
            '/login.indd', '/login.inx', '/login.idml', '/login.odg', '/login.odt', '/login.ods',
            '/login.odp', '/login.odg', '/login.odf', '/login.ott', '/login.ots', '/login.otp',
            '/login.odg', '/login.php?login', '/login.html?login', '/login.jsp?login', '/login.asp?login',
            '/login.aspx?login', '/login.cgi?login', '/login.php3?login', '/login.py?login',
            '/login.rb?login', '/login.pl?login', '/login.sh?login', '/login.bat?login', '/login.exe?login',
            '/login.jar?login', '/login.war?login', '/login.xml?login', '/login.json?login',
            '/login.yaml?login', '/login.yml?login', '/login.txt?login', '/login.md?login',
            '/login.css?login', '/login.js?login', '/login.svg?login', '/login.gif?login',
            '/login.png?login', '/login.jpg?login', '/login.jpeg?login', '/login.ico?login',
            '/login.svgz?login', '/login.webp?login', '/login.avif?login', '/login.tiff?login',
            '/login.tif?login', '/login.bmp?login', '/login.psd?login', '/login.eps?login',
            '/login.ai?login', '/login.indd?login', '/login.inx?login', '/login.idml?login',
            '/login.odg?login', '/login.odt?login', '/login.ods?login', '/login.odp?login',
            '/login.odg?login', '/login.odf?login', '/login.ott?login', '/login.ots?login',
            '/login.otp?login', '/login.odg?login', '/login.php?login=', '/login.html?login=',
            '/login.jsp?login=', '/login.asp?login=', '/login.aspx?login=', '/login.cgi?login=',
            '/login.php3?login=', '/login.py?login=', '/login.rb?login=', '/login.pl?login=',
            '/login.sh?login=', '/login.bat?login=', '/login.exe?login=', '/login.jar?login=',
            '/login.war?login=', '/login.xml?login=', '/login.json?login=', '/login.yaml?login=',
            '/login.yml?login=', '/login.txt?login=', '/login.md?login=', '/login.css?login=',
            '/login.js?login=', '/login.svg?login=', '/login.gif?login=', '/login.png?login=',
            '/login.jpg?login=', '/login.jpeg?login=', '/login.ico?login=', '/login.svgz?login=',
            '/login.webp?login=', '/login.avif?login=', '/login.tiff?login=', '/login.tif?login=',
            '/login.bmp?login=', '/login.psd?login=', '/login.eps?login=', '/login.ai?login=',
            '/login.indd?login=', '/login.inx?login=', '/login.idml?login=',
            '/login.odg?login=', '/login.odt?login=', '/login.ods?login=', '/login.odp?login=',
            '/login.odg?login=', '/login.odf?login=', '/login.ott?login=', '/login.ots?login=',
            '/login.otp?login=', '/login.odg?login='
        ]
        for patch in common_login_patch:
            test_urlNya = url(urljoin(url, patch))
            try:
                test_pagenya = requests.get(test_urlNya, headers=hdrs, timeout=6)
                if test_pagenya.status_code == 200:
                    test_soupnya = BeautifulSoup(test_pagenya.text, 'html.parser')
                    forms = test_soupnya.find_all('form')
                    
                    for form in forms:
                        inputs = form.find_all('input')
                        has_user = any(i.get('name', '').lower() in ['username', 'email', 'user'] for i in inputs)
                        has_passwd = any(i.get('type', '').lower() == 'password' for i in inputs)
                        
                        if has_user and has_passwd:
                            return {
                                'login_urls' : test_urlNya,
                                'login_forms' : [{
                                    'action' : form.get('action', ''),
                                    'method' : form.get('method', 'get').upper(),
                                    'inputs' : [{'name' : i.get('name'), 'type' : i.get('type')} for i in inputs]
                                }],
                                'status' : 'login page ditemukan',
                            }
            except requests.RequestException:
                continue
        return {
        'status': f"{LRD}tidak ada halaman login ditemukan!{X}"
    }
    except requests.RequestException as err:
        return {
        'status': f"{LRD}Error: {err}{X}\n{RD}Tidak dapat mengakses URL atau tidak valid{X}"
    }
    except Exception as eror2_status2:
        return {
        'status': f"{LRD}Error: {eror2_status2}{X}\n{RD}Terjadi kesalahan saat memproses URL{X}"
    }


#--------------- MAIN ---------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <URL>")
        sys.exit(1)
       
    target = sys.argv[1]    
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    Wlecome(Ctext=logoScript, Thitungan=5)
    print(f"{LMAGENTA}Target URL: {LGN} {target}{X}")
    hasilUrl = URLFinder(target)
    
    print(f"{LGN}\n Results: ")
    if 'error' in hasilUrl:
        print(f"{X}{LRD}Error: {hasilUrl['error']}{X}")
    else:
        if 'login_urls' in hasilUrl:
            print(f"{LGN}Login URL: {hasilUrl['login_urls']}{X}")
            for form in hasilUrl.get('login_forms', []):
                print(f"{LGN}\nLogin Form:")
                print(f"Action: {form['action']}")
                print(f"Method: {form['method']}")
                print(f"Inputs fields:{X}")
                for field in form['inputs']:
                    print(f" - Name: {field['name']}, Type: {field['type']}")
        else:
            print(f"{LRD}Halaman Tidak Ditemukan!.{X}")
    
    print(f"\nStatus: {hasilUrl.get('status', 'Tidak ada status yang tersedia')}{X}")