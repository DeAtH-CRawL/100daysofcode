import random
import os
import card_art
print(card_art.logo)
def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]  # 11 = Ace
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    # Handle Ace
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    os.system('cls' if os.name == 'nt' else 'clear')

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'hit' to hit, 'stand' to stand: ").lower()
            if choice == 'hit':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n--- Final Results ---")
    print(f"Your hand: {user_cards}, score: {user_score}")
    print(f"Computer's hand: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))

# Replay loop
while input("\nPlay Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
print("Goodbye! Thanks for playing.")
