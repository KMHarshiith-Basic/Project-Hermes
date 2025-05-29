import random

# For the word scramble and Caesar cipher puzzles, we will use the NLTK library to get a list of words.
import nltk
from nltk.corpus import words


nltk.download('words')

word_list = words.words()

words = random.sample(word_list, 100)

hints = ['no of corners of circle', 'beggining', 'the only even prime','triangle','the only number spelled with same no of letters as its value',
           'no of rings in olympics flag','faces of cube','thala for a reason','no of planets in solar system','atomic number of fluorine',]

print("-----------------------------------------------------------------------------")

def Number_Guessing():

    print("Find the number.")
    print("Here are your hints for the digits:")

    global hints

    digit = random.randint(100, 1000000)

    digilist = [int(d) for d in str(digit)]

    for i in range(0,len(digilist)):
        x = digilist[i]
        print(str(i+1)+'. '+hints[x])

    ans = int(input("Enter the digit: "))

    if ans == digit:
        print("Correct!")
        print("-----------------------------------------------------------------------------")
    else:   
        print("Incorrect! The correct answer was:", digit)
        print("-----------------------------------------------------------------------------")




def Word_Scramble():
    
   word = random.choice(words)

   jumbled_word = list(word)
   random.shuffle(jumbled_word)
    
   jumbled_word = ''.join(jumbled_word)
    
   print("Jumbled word : ", jumbled_word)
    
   ans = input("Your answer : ")
    
   if ans == word:
      print("Correct!")
      print("-----------------------------------------------------------------------------")

   else:
      print("Incorrect! the correct answer was:", word)
      print("-----------------------------------------------------------------------------")




def Caesar_Cipher(): 
    result = []
    no = random.randint(1,2)
    randomword= random.choice(words)
    for char in randomword:         
        next_char = chr(ord(char) + no) 
        result.append(next_char) 
    
    print(''.join(result))
    
    answer = input("enter:")

    if answer==randomword:
        print("Correct!!!")
        print("-----------------------------------------------------------------------------")

    else:
        print("Incorrect! The correct answer was:", randomword)
        print("-----------------------------------------------------------------------------")




Number_Guessing()
Word_Scramble()
Caesar_Cipher()