import random
from colorama import Fore, init
from Utilities import wordlist
from Utilities import hints
init(autoreset=True)

words = wordlist.get_words()
hints = hints.get_hints()

def Number_Guessing(I):

    print("Node IP: 192.168.X.?? – Resolve the missing digits.")
    print("Here are your hints for the digits:")

    global hints

    digit = random.randint(100, 1000000)

    digilist = [int(d) for d in str(digit)]
    
    random_no = random.randint(0,2)

    for i in range(0,len(digilist)):
        x = digilist[i]
        print(str(i+1)+'. '+hints[x][random_no])
    if I==1:
        print(' ', end = '')
        print(Fore.LIGHTBLACK_EX + str(digit))
    ans = input("Enter the number: ")

    if ans.strip() == str(digit).strip():
        print("Correct!")
        return 1
    else:   
        print("Incorrect! The correct answer was:", digit)
        return 0

def Word_Scramble(I):
   global words
   word = random.choice(words)

   jumbled_word = list(word)
   random.shuffle(jumbled_word)
    
   jumbled_word = ''.join(jumbled_word)
   print('Someone jammed this text — unscramble before it’s lost.') 
   print("Jumbled word : ", jumbled_word, end = ' ')
   if I==1:
        print(Fore.LIGHTBLACK_EX + word)
   else:
        print('')
   ans = input("Your answer : ").strip()
    
   if ans == word:
      print("Correct!")
      return 1
   else:
      print("Incorrect! the correct answer was:", word)
      return 0

def Caesar_Cipher(I): 
    global words
    result = []
    no = random.randint(1,2)
    randomword= random.choice(words).lower()
    for char in randomword:         
        next_char = chr((ord(char) - ord('a') + no) % 26 + ord('a'))
        result.append(next_char) 
    print('Incoming encrypted message intercepted. Decoding key unknown.')
    print('Encrypted message:', ''.join(result), end = ' ')
    if I==1:
        print(Fore.LIGHTBLACK_EX + randomword)
    else:
        print('')
    
    answer = input("Enter the Decode:").strip()

    if answer.lower()==randomword:
        print("Correct!!!")
        return 1
    else:
        print("Incorrect! The correct answer was:", randomword)
        return 0