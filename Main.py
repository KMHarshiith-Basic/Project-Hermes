import pyfiglet
import time
import random
from Utilities import Fun_GUI
from data import UserInfo
from Utilities import Puzzles
from Utilities import utils
from Utilities.Bot import AI_Bot
from colorama import Fore, Style, init
init(autoreset=True)

title = pyfiglet.figlet_format("CyberHunt Lite", font="slant")
bot = AI_Bot.MiniMind()
b=1

# Game start function and logics
def start(I):
    utils.clear_screen()
    print(Fore.MAGENTA + title)
    utils.print_border(60)
    print(Fore.GREEN + "Game Loading...".center(60))
    R = UserInfo.get_ratings(I)
    utils.print_border(60)

    time.sleep(2)  # Simulate game start delay
    print(Fore.YELLOW + "You are now in the CyberHunt world!".center(60))
    print(Fore.CYAN + "We have these misterious codes, crack them, and find the Cyber Assassin!".center(60))

    A=list(Puzzles.Word_Scramble(I),bot.solve_scramble(R[1]))  # Start the first puzzle
    UserInfo.result1(I,A[0],A[1])  # Store the result of the first puzzle
    utils.print_border()
    print(Fore.GREEN + "Puzzle 1 completed!".center(60))
    print(Fore.YELLOW + "Now, let's see if you can beat the bot in the next challenge.".center(60))
    time.sleep(2)  # Simulate a delay before the next challenge

    B=list(Puzzles.Number_Guessing(I),bot.solve_number_guess(R[2]))  # Start the second puzzle
    UserInfo.result2(I,B[0],B[1])  # Store the result of the second puzzle
    utils.print_border()
    print(Fore.GREEN + "Puzzle 2 completed!".center(60))
    print(Fore.YELLOW + "Now, you are ready to find the Cyber Assassin!".center(60))
    time.sleep(2)  # Simulate a delay before the final challenge

    C=list(Puzzles.Caesar_Cipher(I),bot.solve_caesar(R[3]))  # Start the third puzzle
    UserInfo.result3(I,C[0],C[1])  # Store the result of the third puzzle
    utils.print_border()
    print(Fore.GREEN + "Puzzle 3 completed!".center(60))
    name = UserInfo.get_data(I)
    print(Fore.YELLOW + f"We have found some information about the Cyber Assassin {name[1]}!".center(60))
    utils.thrill()
    print('Location of the Cyber Assassin cracked...')
    print('Be QUICK to catch him.')
    D=UserInfo.get_data(I)
    B=Fun_GUI.Boss(R[4])
    if B == 1:
        print(f"Don't worry {D[1]}, let's defeat the Assassin in our next trial together")
        input('Press Enter to continue...')
        end()
    elif B == 0:
        print("Congrats, we made it...")
        input('Press Enter to continue...')
        end()

def end():
    global b
    utils.clear_screen()
    width = 35
    #utils.print_border(width+65)
    print(Fore.GREEN + title)
    utils.print_border(width+65)
    end = input("Press Enter to play again (or) Q to quit...")
    if end == 'Q' or end == 'q':
        print(Fore.RED + "\nQuitting the experience...")
        time.sleep(random.random()*2+1.5)  # Simulate a delay for dramatic effect
        print(Fore.CYAN + "Closing the game...")
        time.sleep(random.random()*2)
        utils.print_border(width+65)
    else:
        b = 1
        welcome_screen(b)

def new_player():
    Try=0
    name = input('Enter your username: ').strip()
    if UserInfo.check(name):
        if Try==0:
            print(Fore.RED + "Username already exists, please choose a different one.")
            input("Press Enter to try again...")
            new_player()
        if Try==1:
            print('Try logging in instead')
            input('Press enter to return to previous page')
            go()
    elif name == '':
        print(Fore.RED + "Username cannot be empty, please try again.")
        new_player()
    else:
        print('Your username will be set as : ' + Fore.GREEN + name)
        con=input('Are you sure? (yes/no): ').strip()
        if con == 'yes' or con == 'y' or con == 'Y' or con == 'Yes' or con == 's' or con == 'S':
            UserInfo.new(name)
            print(Fore.GREEN + f"Welcome {name}, let's start the game!")
            print('Your username: ' + Fore.GREEN + name, 'Your ID: ' + Fore.GREEN + str(UserInfo.id(name)))
            input("Press Enter to continue...")
            start(UserInfo.id(name))
        else:
            print(Fore.RED + "Username not set, please try again.")
            new_player()

def go():
    utils.clear_screen()
    print(title)
    utils.print_border(60)
    print('new player(1) or existing player(2)?')
    choice= input('Enter your choice: ').strip()
    if choice == '1':
        new_player()
    elif choice == '2':
        name = input('Enter your username: ')
        if UserInfo.check(name):
            print(Fore.GREEN + f"Welcome back {name}, let's continue the game!")
            time.sleep(2)
            start(UserInfo.id(name))
        else:
            print(Fore.RED + "Username not found, please try again.")
            input("Press Enter to continue...")
            go()
    else:
        print(Fore.RED + "Invalid choice, please try again. (only 1 or 2 are accepted)")
        input("Press Enter to continue...")
        go()

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
    utils.print_centered("3. Get Your Info", width)
    utils.print_centered("4. Exit", width)
    utils.print_border(width+65)
    choice = input("Enter your choice: ".center(width)).strip()
    if choice == '1':
        print(Fore.GREEN + "\nStarting game...".center(width))
        time.sleep(random.random()*3) # Simulate a delay for dramatic effect
        go()  # Game start function
    elif choice == '2':
        b=0
        print(Fore.YELLOW + "\nInstructions: Solve puzzles, Beat the bot, Find the Cyber Assassin".center(width))
        input("\nPress Enter to return to menu.".center(width))
        welcome_screen(b)
    elif choice == '4':
        print(Fore.RED + "\nQuitting the experience...")
        time.sleep(random.random()*2+1.5)  # Simulate a delay for dramatic effect
        print(Fore.CYAN + "Closing the game...")
        time.sleep(random.random()*2)
        utils.print_border(width+65)
    elif choice == '3':
        info = UserInfo.get_data(UserInfo.id(input("Enter your username: ").strip()))
        if info:
            print(Fore.CYAN + "\nYour Info:".center(width))
            utils.print_border(width)
            print(Fore.GREEN + f"Username: {info[1]}\nUser ID: {info[0]}\nPlayed: {info[2]}\nRating1: {info[4]}\nRating2: {info[5]}\nRating3: {info[6]}".center(width))
            utils.print_border(width)
            input("Press Enter to return to menu.".center(width))
            welcome_screen(b)
        else:
            print(Fore.RED + "\nUser not found, please try again.".center(width))
            input("Press Enter to return to menu.")
            welcome_screen(b)
    else:
        print(Fore.RED + "\nInvalid choice, try again.".center(width))
        input("Press Enter to continue.".center(width))
        welcome_screen(b)

welcome_screen()