import random

words_6_characters=['actual','across','afraid','agency','afford','action','agenda','always']
words_10_characters=['strawberry','friendship','everything','appreciate','motivation','jazzercise','maximizing','minimizing']

user_input=input("Enter Your Name: ")
user_choice=int(input("\nChose from following Options: \n 1. 6 Character Word Guess \n 2. 10 Character Word Guess \n"))
p=0 # testing variable used in for loop
c=10 # counting variable used for guessing numbers
if user_choice==1: 
        print("\n*** Welcome to 6 Character Word Guess Game ***")
        word=random.choice(words_6_characters)
        for count in range(0,10):
                user_input1=input("Enter a Character to guess the word: ")
                if user_input1 in word:
                        c-=1
                        print(" \nWell Done, Congratulations You Guessed Correct ")
                        print(" Index of character is : ",word.index(user_input1))
                        print("The random word selected is: ",word)
                        print("")
                        p=1
                        break
                elif user_input1 not in word:
                        c-=1
                        print("\nRemaining Guesses : ",c)
                        continue
        if p==0:
                print("\nSorry Better Luck Next Time")
elif user_choice==2:
        print("\n*** Welcome to 10 Character Word Guess Game ***")
        word=random.choice(words_10_characters)
        for count in range(0,10):
                user_input1=input("Enter a Character to guess the word: ")
                if user_input1 in word:
                        c-=1
                        print(" \nWell Done, Congratulations You Guessed Correct ")
                        print(" Index of character is : ",word.index(user_input1))
                        print("The random word selected is: ",word)
                        print("")
                        p=1
                        break
                elif user_input1 not in word:
                        c-=1
                        print("\nRemaining Guesses : ",c)
                        continue
        if p==0:
                print("\nSorry Better Luck Next Time")
else:
        print("\nInvalid Input")


