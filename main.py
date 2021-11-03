from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, number, turns):
    if guess < number:
        print("Too low.")
        return turns - 1
    elif guess > number:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != number:
        print(
            f"You have {turns} attempts remaining to guess the number. Make them count.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)  # VRACI CISLO!!!!!
        if turns == 0:
            print("You've run out of guesses. LOSER!!!")
            return


game()
