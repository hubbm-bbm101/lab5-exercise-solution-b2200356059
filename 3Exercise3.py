import random
number =random.randint(1,100)
guess = ""
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number: print("increase your number")
    elif guess > number: print("decrease your number")    

print("It's correct!")