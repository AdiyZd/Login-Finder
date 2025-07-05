import os
import time
import subprocess
import sys

X = "\033[0m" # Reset warna
GR = "\033[90m" # Abu-abu
LRD = "\033[91m" # Merah terang
LGN = "\033[92m" # Hijau terang
LYW = "\033[93m" # Kuning terang
LBL = "\033[94m" # Biru terang
LMAGENTA = "\033[95m" # Magenta terang
LCYAN = "\033[96m" # Cyan terang
Lw = "\033[97m" # Putih terang

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
time.sleep(1)
print(f"{LGN}Melakukan instalasi module, silahkan tunggu...{X}")
time.sleep(1)
print(f"{GR}={X}"*50)

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
except subprocess.CalledProcessError:
    print(f"{LRD}Gagal menginstal requirements. Cek file requirements.txt dan koneksi internet.{X}")
