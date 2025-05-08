import random

# random.seed(21)

print("I am thinking of a number between 1 and 20.")

num = random.randrange(1, 21, 1)

guess = input("What's your guess?")

while True:
    if guess.lower() == 'x':
        break

    n = 0
    try:
        n = int(guess)
    except ValueError:
        print("Please enter an integer number")

    if n != num:
        guess = input("Unfortunately, that isn't the number. Try another guess: ")
    else:
        print(f"Yes! The number is indeed {n}!")
        break

print("Thanks for playing!")
        
