import random

# random.seed(21)

print("I have thought of a number between 1 and 20.")

num = random.randrange(1, 21, 1)

inp = input("What's your guess?")

n = 0
try:
    n = int(inp)
except ValueError:
    print("Please enter an integer number")

if n > num:
    print(f"Unfortunately, that wasn't the number. It was {num}, and your guess was greater by {abs(n - num)}")
elif n < num:
    print(f"Unfortunately, that wasn't the number. It was {num}, and your guess was smaller by {abs(n - num)}")
else:
    print(f"Yes! The number was indeed {n}!")

