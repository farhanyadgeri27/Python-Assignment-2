# Q16 - Number Guessing Game

import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempt = 1

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.\n")

while attempt <= max_attempts:
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the correct number.")
            print("Number of attempts used:", attempt)
            break

        elif guess < secret_number:
            print("Too low! Try again.\n")

        else:
            print("Too high! Try again.\n")

        attempt += 1

    except ValueError:
        print("Please enter a valid number.\n")

if attempt > max_attempts:
    print("❌ Game Over!")
    print("The correct number was:", secret_number)