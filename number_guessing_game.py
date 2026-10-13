import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts = attempts + 1

        if guess > number:
            print("Too high! Try again.")
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("You won!")
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a number.")  
