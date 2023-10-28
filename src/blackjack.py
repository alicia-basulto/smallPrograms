##TO DO

import random

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
def blackjack():
    def calculate_score(cards):
        score = 0
        # Blackjack
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        score = sum(cards)
        # 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            score -= 10

        return score

    # Hint 13: Create a function called compare() and pass in the user_score and computer_score.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses.
    # If the user has a blackjack (0), then the user wins.
    # If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if user_score > 21:
            print("You lose")
        elif computer_score > 21:
            print("You win")
        elif user_score == 0:
            print("Blackjack! You win")
        elif user_score == computer_score:
            print("Draw")
        elif computer_score == 0:
            print("Blackjack! You lose")
        elif computer_score > user_score:
            print("You lose")
        else:
            print("You win")
    def deal_card():
     return random.choice(cards)


    #11 is the Ace.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's cards: {computer_cards[0]}")
    user_option = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_option == "y":
        user_cards.append(deal_card())

    compare(calculate_score(user_cards), calculate_score(computer_cards))


