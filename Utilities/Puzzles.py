import random
from wordlist import words
from hints import hints

print("-----------------------------------------------------------------------------")

def Number_Guessing():

    print("Find the number.")
    print("Here are your hints for the digits:")

    global hints

    digit = random.randint(100, 1000000)

    digilist = [int(d) for d in str(digit)]
    
    random_no = random.randint(0,3)

    for i in range(0,len(digilist)):
        x = digilist[i]
        print(str(i+1)+'. '+hints[x][random_no])

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




#Number_Guessing()
#Word_Scramble()
#Caesar_Cipher()