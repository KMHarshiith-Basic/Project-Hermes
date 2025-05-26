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
