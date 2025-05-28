import pyfiglet
import time
import random
from Utilities import UserData
from Utilities import Puzzles
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
    time.sleep(2)  # Simulate game start delay
    print(Fore.YELLOW + "You are now in the CyberHunt world!".center(60))
    print(Fore.CYAN + "We have these misterious codes, crack them, and find the Cyber Assassin!".center(60))
    A=list(Puzzles.puzzle1())  # Start the first puzzle
    UserData.result(A)  # Store the result of the first puzzle
    print(Fore.GREEN + "Puzzle 1 completed!".center(60))
    print(Fore.YELLOW + "Now, let's see if you can beat the bot in the next challenge.".center(60))
    time.sleep(2)  # Simulate a delay before the next challenge
    B=list(Puzzles.puzzle2())  # Start the second puzzle
    UserData.result(B)  # Store the result of the second puzzle
    print(Fore.GREEN + "Puzzle 2 completed!".center(60))
    print(Fore.YELLOW + "Now, you are ready to find the Cyber Assassin!".center(60))
    time.sleep(2)  # Simulate a delay before the final challenge
    C=list(Puzzles.puzzle3())  # Start the third puzzle
    UserData.result(C)  # Store the result of the third puzzle
    print(Fore.GREEN + "Puzzle 3 completed!".center(60))
    print(Fore.YELLOW + "We have found some information about the Cyber Assassin!".center(60))
    utils.thill()

def end():
    input("Press Enter to play again...")
    b=1  # Reset welcome screen flag
    welcome_screen()

b=1
#welcome screen
def welcome_screen(a=1):
    global b
    utils.clear_screen()
    width = 35
    #utils.print_border(width+65)
    print(Fore.MAGENTA + title)
    utils.boxed("welcome to your next cyber trial.\nReady to play?")
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