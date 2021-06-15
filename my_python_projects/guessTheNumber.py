import random

def guessTheNumber(x):
    random_num = random.randint(1,x)
    guess = 0

    while guess != random_num:
        guess =int( input(f"Guess the number between 1 and {x} "))
        if guess < random_num:
            print("Sorry guess again. Too low!!")
        elif guess > random_num:
            print("Sorry guess again.Too High!!")
        else:
            print(f"Congratulation you guessed the number {random_num} correctly!!! ")

def computer_Guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high (H) or too low (L) or correct (C)?")
        if feedback == 'H' or feedback == 'h':
            high = guess - 1
        elif feedback=='L' or feedback=='l':
            low = guess+1
        else:
            print(f"hurray!!! Computer guessed your, {guess} number correctly")

#guessTheNumber(10)
computer_Guess(100)