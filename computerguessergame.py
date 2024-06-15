print("hello welcome to computer guesser!")
print(input("press any key to start: "))

user_name = ""
while len(user_name) == 0:
    user_name = input("enter your name pls: ")
print("hello "+user_name)
print("")
print("pls pick a difficulty level")
level_choice = int(input("for level 1 (1-10) pls type number 1 , for level 2 (1-50), pls type number 2 , for level 3 (1-100), pls type number 3 : "))

import random

if level_choice < 1 and level_choice > 3:
    print("that is not a difficult level")

if level_choice == 1:
    computer_guess = str(random.randint(1,10))
    user_guess = input("pls guess a number from 1-10: ")
    print("the computers guess is "+computer_guess)
    print("ur guess is "+ str(user_guess))

elif level_choice == 2:
    computer_guess = str(random.randint(1,50))
    user_guess = input("pls guess a number from 1-50: ")
    print("the computers guess is "+computer_guess)
    print("ur guess is "+ str(user_guess))

elif level_choice == 3:
    computer_guess = str(random.randint(1,100))
    user_guess = input("pls guess a number from 1-100: ")
    print("the computers guess is "+computer_guess)
    print("ur guess is "+ str(user_guess))   

if user_guess == computer_guess:
    print("congrats you have won!!")
else:
 print("you lost,try again")    