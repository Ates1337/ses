#coded by ates
from gtts import gTTS
from playsound import playsound
from colorama import Fore
import os


os.system("clear")
print("  █████╗ ████████╗ ██████╗ ██╗     ██╗")
print(" ██╔══██╗╚══██╔══╝██╔═══██╗██║     ██║")
print(" ███████║   ██║   ██║   ██║██║     ██║")
print(" ██╔══██║   ██║   ██║   ██║██║     ██║")
print(" ██║  ██║   ██║   ╚██████╔╝███████╗██║")
print(" ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝")
                                     
dosya = input(Fore.RED + "Dosya İsmi Giriniz: ")


os.system("clear")
print("  █████╗ ████████╗ ██████╗ ██╗     ██╗")
print(" ██╔══██╗╚══██╔══╝██╔═══██╗██║     ██║")
print(" ███████║   ██║   ██║   ██║██║     ██║")
print(" ██╔══██║   ██║   ██║   ██║██║     ██║")
print(" ██║  ██║   ██║   ╚██████╔╝███████╗██║")
print(" ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝")
ses = input(Fore.RED + "Yazı Giriniz: ")


os.system("clear")
print("\n\n\n\n\n")
print(Fore.YELLOW + "Örnek Türkiye > tr | İngilizce > en")
print("\n\n\n\n\n")
dil = input(Fore.RED + "Dil Seçeneği Giriniz: ")


wytron = gTTS(text=ses,
          lang= dil,slow=False)


ato = (dosya + '.mp3')
wytron.save(ato)
os.system("clear")
os.system("xdg-open " + ato)
