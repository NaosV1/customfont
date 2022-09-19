import re
import sys
import os
import time
from art import *
from colorama import init, Fore, Back, Style
init()

def main():
	if len(sys.argv) != 2:
		os.system("cls")
		os.system("color f")
		print(Fore.MAGENTA + "\n\n░█████╗░██╗░░░██╗░██████╗████████╗░█████╗░███╗░░░███╗███████╗░█████╗░███╗░░██╗████████╗ ")
		print(Fore.MAGENTA + "██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██╔══██╗████╗░████║██╔════╝██╔══██╗████╗░██║╚══██╔══╝ ")
		print(Fore.MAGENTA + "██║░░╚═╝██║░░░██║╚█████╗░░░░██║░░░██║░░██║██╔████╔██║█████╗░░██║░░██║██╔██╗██║░░░██║░░░ ")
		print(Fore.MAGENTA + "██║░░██╗██║░░░██║░╚═══██╗░░░██║░░░██║░░██║██║╚██╔╝██║██╔══╝░░██║░░██║██║╚████║░░░██║░░░ ")
		print(Fore.MAGENTA + "╚█████╔╝╚██████╔╝██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░░░░╚█████╔╝██║░╚███║░░░██║░░░ ")
		print(Fore.MAGENTA + "░╚════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░ \n\n")
		file = input(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "CustomFont" + Fore.LIGHTYELLOW_EX + "]" + Fore.WHITE + " Merci de préciser un texte : ")
		if not file:
			print(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "CustomFont" + Fore.LIGHTYELLOW_EX + "]" + Fore.WHITE + " Aucun text entrée")
			sys.exit(1)
		a = 0
		while a != 100:
			a += 1
			time.sleep(0.1)
			tprint(file, font="random")
		print(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "CustomFont" + Fore.LIGHTYELLOW_EX + "]" + Fore.WHITE + " 100 Polices différente ont été généré")
		

if __name__ == "__main__":
	main()
	sys.exit(0)
	

