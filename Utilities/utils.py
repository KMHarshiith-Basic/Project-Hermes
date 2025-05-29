import os
import sys
# Temporarily suppress stdout
original_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame
# Restore stdout
sys.stdout.close()
sys.stdout = original_stdout

def boxed(text):
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    print("+" + "-" * (width + 2) + "+")
    for line in lines:
        print("| " + line.ljust(width) + " |")
    print("+" + "-" * (width + 2) + "+")

def clear_screen():
    # Back from the 90s, this works cross-platform for clearing terminal like C++
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, width=60):
    print(text.center(width))

def print_border(width=60):
    print("=" * width)

def thill():
    # Simulate a thrilling sound effect
    import time
    import random
    sounds = ["Beep...", "Bzzz...", "Ding!", "Ping!", "Buzz..."]
    music = ["sounds/beep.mp3", "sounds/bzzz.mp3", "sounds/ding.mp3", "sounds/ping.mp3", "sounds/buzz.mp3"]
    for i in range(6):
        print(sounds[i-1])
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(music[i-1])
        pygame.mixer.music.play()
        time.sleep(random.uniform(0.5, 1.5))  # Random delay between sounds