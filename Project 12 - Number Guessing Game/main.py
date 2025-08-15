import art
import random

def compare(guess, answer):
    if guess > answer:
        print("Too high.")
    if guess < answer:
        print("Too low.")
    if guess == answer:
        print(f"You got it! The number was {answer}")

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1,100)

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    while game_difficulty != "easy" and game_difficulty != "hard":
        print("Invalid difficulty. Try again.")
        game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_difficulty == "easy":
        lives = 10
    elif game_difficulty == "hard":
        lives = 5

    print(f"You have {lives} remaining to guess the number")

    while lives != 0:
        guess = int(input("Make a guess: "))

        if guess != number:
            lives -= 1
            compare(guess, number)
            print("Guess again")
            print(f"You have {lives} lives remaining to guess the number")
        else:
            compare(guess, number)
            lives = 0
play_game()