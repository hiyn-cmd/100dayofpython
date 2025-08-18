import art
import game_data
import random

def format_data(dict):
    name = dict["name"]
    description = dict["description"]
    country = dict["country"]
    return f"{name}, a {description}, from {country}."

def compare(a,b):
    if a > b:
        return "a"
    else:
        return "b"

account_b = random.choice(game_data.data)
game_should_continue = True
print(art.logo)
score = 0

while game_should_continue:
    account_a = account_b
    account_b = random.choice(game_data.data)

    print(f"Compare A. {format_data(account_a)}")
    print(art.vs)
    print(f"Against B. {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == compare(account_a["follower_count"], account_b["follower_count"]):
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
