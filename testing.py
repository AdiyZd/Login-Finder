import os
from pyfiglet import Figlet

# Truecolor RGB helper
def RGB(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

X = "\033[0m"

# Preset warna
YELLOW_GOLD = RGB(255, 215, 0)
NEON_GREEN  = RGB(0, 255, 0)
SKY_BLUE    = RGB(0, 191, 255)
CYAN_BRIGHT = RGB(0, 255, 255)
PINK        = RGB(255, 0, 255)
HOT_PINK    = RGB(255, 105, 180)
DEEP_PINK   = RGB(255, 20, 147)
VIOLET      = RGB(138, 43, 226)
INDIGO      = RGB(75, 0, 130)

fig = Figlet(font='slant')
text1 = fig.renderText('Login')
text2 = fig.renderText('Finder')


colored_logo = (
    f"{YELLOW_GOLD}{text1}{CYAN_BRIGHT}{text2}{X}"
)

# Fungsi center di terminal
def print_centered(text):
    lines = text.split('\n')
    width = os.get_terminal_size().columns
    for line in lines:
        print(line.center(width))

print_centered(colored_logo)
