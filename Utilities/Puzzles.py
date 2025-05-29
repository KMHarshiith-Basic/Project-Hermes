import random
from Bot import AI_Bot
# For the word scramble and Caesar cipher puzzles, we will use the NLTK library to get a list of words.
import nltk
from nltk.corpus import words


nltk.download('words')
bot = AI_Bot.MiniMind([])
word_list = words.words()

words = random.sample(word_list, 100)

hints = ['Number of corners of circle', 'The Beggining', 'The only even prime','Triangle','The only number spelled with same number of letters as its value',
           'Number of rings in olympics flag','Number of faces of a cube','Thala for a reason','Number of planets in solar system','Atomic number of fluorine',]

def Number_Guessing():

    print("We have some clues about the IP address of the Assassin.")
    print("Here are your hints for the digits:")

    global hints

    digit = random.randint(100, 1000000)

    digilist = [int(d) for d in str(digit)]

    for i in range(0,len(digilist)):
        x = digilist[i]
        print(str(i+1)+'. '+hints[x])

    ans = int(input("Enter the Number: "))

    if ans == digit:
        print("Correct!")
    else:   
        print("Incorrect! The correct answer is:", digit)




def Word_Scramble():
    
   word = random.choice(words)

   jumbled_word = list(word)
   random.shuffle(jumbled_word)
    
   jumbled_word = ''.join(jumbled_word)
    
   print('These mixed up letters have potential of revealing some information...')
   print("Jumbled word : ", jumbled_word)
    
   ans = input("Your answer: ")
    
   if ans.lower() == word.lower():
      print("Correct!")

   else:
      print("Incorrect! the correct answer is:", word)




def Caesar_Cipher(): 
    result = []
    no = random.randint(1,3)
    randomword= random.choice(words).lower()
    for char in randomword:         
        next_char = chr(ord(char) + no) 
        result.append(next_char) 
    
    print(''.join(result))
    print('This message was encripted with some kind of Cipher code, it could be related to the Assassin.')
    answer = input("Enter the decoded word:")

    if answer.lower()==randomword.lower():
        print("Correct!!!")

    else:
        print("Incorrect! The correct answer is:", randomword)