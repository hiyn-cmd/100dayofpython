import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10]


def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards_list):
    total = sum(cards_list)
    if 10 in cards_list and 11 in cards_list and len(cards_list) == 2:
        return 0

    elif 11 in cards_list and total > 21:
        cards_list.remove(11)
        cards_list.append(1)

    else:
        return total

def compare(player_1, player_2):
    if calculate_score(player_2) == 0:
        return "Lose, opponent has Blackjack"
    elif calculate_score(player_1) == calculate_score(player_2):
        return "Draw"
    elif calculate_score(player_1) == 0:
        return "Win with a Blackjack"
    elif calculate_score(player_1) > 21:
        return "You went over. You lose"
    elif calculate_score(player_2) > 21:
        return "Opponent went over. You win"
    elif calculate_score(player_1) > calculate_score(player_2):
        return "You win"
    elif calculate_score(player_1) < calculate_score(player_2):
        return "You lose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour cards: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final card: {computer_cards}, final score: {computer_score}")
    print(computer_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()