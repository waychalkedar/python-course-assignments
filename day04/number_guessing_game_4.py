import random

# random.seed(21)

print("I am thinking of a number between 1 and 20.")

num = random.randrange(1, 21, 1)

debug_on = False

while True:
    if debug_on:
        print(f"The current number is {num}.")
    guess = input("What's your guess? ")

    if guess.lower() == 'x':
        break

    if guess.lower() == 's':
        print(f"You found the cheat key :) The number I am thinking of is {num}.")
        continue

    if guess.lower() == 'd':
        if not debug_on: 
            print(f"You have entered debug mode.")
            debug_on = not debug_on
            continue
        else:
            print("You have exited debug mode.")
            debug_on = not debug_on
            continue

    n = 0
    try:
        n = int(guess)
    except ValueError:
        print("Please enter an integer number")
        continue

    if (n != num) and (guess.lower() != 's'):
        print("Unfortunately, that isn't the number. Try again!")
    else:
        print(f"Yes! The number is indeed {n}!")
        break

print("Thanks for playing!")


