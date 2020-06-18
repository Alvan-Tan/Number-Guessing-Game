import random

print("NUMBER GUESSING GAME")

answer = random.randint(1,100)
lower = 1
upper = 100

max_tries = 7

guess = input("Guess a number between 1 and 100 inclusive (Type 'END' to see answer)")

while max_tries>0:
    if guess == "END":
        print(f"The answer is {answer}, better luck next time")
        break
    elif int(guess) == answer:
        print("Congrats you win!")
        break
    elif int(guess) > answer:
        upper = int(guess) - 1
        guess = input(f"Your guess was too high: Guess another number between {lower} and {upper} inclusive (Type 'END' to see answer)")
    elif int(guess) < answer:
        lower = int(guess) + 1
        guess = input(f"Your guess was too low: Guess another number between {lower} and {upper} inclusive (Type 'END' to see answer)")

    max_tries -= 1
    print(f"You have {max_tries} chances left")