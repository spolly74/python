# imports
import random

# define variables
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards=[]
dealer_cards=[]
your_score = sum(your_cards)
dealer_score = sum(dealer_cards)
your_blackjack = ""
dealer_blackjack = ""

#start the game
from art import logo


def end_game():
    your_score = sum(your_cards)
    dealer_score = sum(dealer_cards)
    print(f"Your final hand: {your_cards}. Your final score: {your_score}")
    print(f"Dealer's final hand: {dealer_cards}. Dealer's score: {dealer_score}")
    if your_blackjack == True:
        print("Blackjack! You win!")
    elif dealer_blackjack == True:
        print("Dealer has blackjack. You lose.")
    elif your_score > dealer_score and your_score < 22:
        print("You win!")
    elif dealer_score > 21 and your_score < 22:
        print("You win!")
    elif dealer_score == your_score and dealer_score < 22 and your_score < 22:
        print("It's a draw.")
    else:
        print("You lose. Better luck next time.")
    play_again = input("Would you like to play again? Enter 'y' or 'n': ").lower
    if play_again == "y":
        start_game()
    elif play_again == "n":
        exit()

def draw_card():
    your_cards.append(random.choice(cards))
    your_score = sum(your_cards)
    if your_score > 21:
        end_game
    else:
        print(f"Your cards are {your_cards}. Your current score is {your_score}.") 
        print(f"Dealer's first card is {dealer_cards[0]}.")
    if dealer_score > 21:
        end_game

    
def start_game():
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        print(logo)

        #drawcards
        for num in range(2):
            your_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))

        #get scores
        your_score = sum(your_cards)
        dealer_score = sum(dealer_cards)

        print(f"Your cards are {your_cards}. Your current score is {your_score}.")
        print(f"Dealer's first card is {dealer_cards[0]}.")

        #check for blackjack
        if your_score == 21 and len(your_score) == 2:
            your_blackjack = True
            end_game()
        elif dealer_score == 21 and len(dealer_cards) == 2:
            dealer_blackjack = True
            end_game()
        #check for aces
        if your_score > 21:
            for card in your_cards:
                if card == 11:
                    card = 1
            your_score = sum(your_cards)
            if your_score > 21:
                end_game()
        if dealer_score > 21:
            for card in dealer_cards:
                if card == 11:
                    card = 1
            dealer_score = sum(dealer_cards)
            if dealer_score > 21:
                end_game()    

        #another card?
        while your_score < 21:
            another_card = input("Would you like another card? Type 'y' or 'n':").lower()
            if another_card == "y":
                draw_card()
            while dealer_score < 17:
                print("Dealer takes a card.")
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
            if another_card == "n": 
                end_game()
start_game()

