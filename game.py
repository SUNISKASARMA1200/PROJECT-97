import random
print ("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 to 9 : ")
while chances < 5:
    guess=int(input("Enter your guess : "))
    if guess== number:
        print("Congratulations you won!!")
        break
    elif guess<number:
        print("your guess is low.Guess a bigger number",guess)
    else :
       print("your guess is high.Guess a smaller number",guess) 
    chances=chances+1

if not chances<5:
    print("YOU LOSE!! The number is : ",number)
