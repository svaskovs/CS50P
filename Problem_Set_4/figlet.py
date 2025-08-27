from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        fnt = random.choice(figlet.getFonts())
        print_fig(fnt)
    elif sys.argv[1] in ("-f", "--font") and len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts():
        print_fig(sys.argv[2])
    else:
        print ("Invalid usage")
        sys.exit(1)
        

def print_fig(fnt):
    text = input("Input: ")
    figlet.setFont(font=fnt)
    print (f"Output: \n{figlet.renderText(text)}")

main()