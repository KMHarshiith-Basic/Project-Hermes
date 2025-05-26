import pyfiglet
import time
import random
from Utilities import utils
from colorama import Fore, Style, init
init(autoreset=True)

title = pyfiglet.figlet_format("CyberHunt Lite", font="slant")

# Game start function and logics
def start():
    utils.clear_screen()
    print(Fore.MAGENTA + title)
    utils.print_border(60)
    print(Fore.GREEN + "Game Loading...".center(60))
    utils.print_border(60)
    # Placeholder for game logic
    time.sleep(2)  # Simulate game start delay
    print(Fore.YELLOW + "You are now in the CyberHunt world!".center(60))
    input("Press Enter to play again...")
    b=1  # Reset welcome screen flag
    welcome_screen()
    # Further game logic would go here

b=1
#Welcom screen
def welcome_screen(a=1):
    global b
    utils.clear_screen()
    width = 35
    #utils.print_border(width+65)
    print(Fore.MAGENTA + title)
    utils.boxed("Welcome to your next cyber trial.\nReady to play?")
    utils.print_centered("1. Start Game", width)
    if a == 1:
        utils.print_centered("2. Instructions", width)
    else:
        utils.print_centered("2. Instructions (read once again)", width)
    utils.print_centered("3. Exit", width)
    utils.print_border(width+65)
    choice = input("Enter your choice: ".center(width)).strip()
    if choice == '1':
        print(Fore.GREEN + "\nStarting game...".center(width))
        time.sleep(random.random()*3) # Simulate a delay for dramatic effect
        start()  # Game start function
    elif choice == '2':
        b=0
        print(Fore.YELLOW + "\nInstructions: Solve puzzles, Beat the bot, Find the Cyber Assasin".center(width))
        input("\nPress Enter to return to menu.".center(width))
        welcome_screen(b)
    elif choice == '3':
        print(Fore.RED + "\nQuiting the experience...")
        time.sleep(random.random()*2+1.5)  # Simulate a delay for dramatic effect
        print(Fore.CYAN + "Closing the game...")
        time.sleep(random.random()*2)
        utils.print_border(width+65)
    else:
        print(Fore.RED + "\nInvalid choice, try again.".center(width))
        input("Press Enter to continue.".center(width))
        welcome_screen(b)

welcome_screen()