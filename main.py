from art import logo
import random

number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty  == "easy":
    attempts = 10
else:
    attempts = 5

game_ended = False
while not game_ended:
    print(f"You have {attempts} attempts remaining to guess the number. Make them count.")
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number}")
        game_ended = True
    
    attempts -= 1
    
    if attempts == 0:
        game_ended = True
        print("You've run out of guesses. LOSER!!!")
