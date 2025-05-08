import random

# random.seed(21)
game = 'n' 

while game.lower() == 'n':
    print("I am thinking of a number between 1 and 20.")

    num = random.randrange(1, 21, 1)

    debug_on = False
    move_on = False

    while True:
        if move_on:
            shift = random.randint(-2, 2)
            num = num + shift

        if debug_on:
            print(f"The current number is {num}.")
        guess = input("What's your guess? ")

        if guess.lower() == 'm':
            if not move_on:
                print("You have entered move mode. The number I am thinking of will now change slightly each time.")
                move_on = not move_on
                continue
            else:
                print("You have exited move mode. The number will now not change from its current value.")
                move_on = not move_on
                continue
        
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

        if n != num:
            print("Unfortunately, that isn't the number. Try again!")
        else:
            print(f"Yes! The number is indeed {n}!")
            break

    game = input("Thanks for playing! Press n to start a new game, or any other button to end this session. ")


