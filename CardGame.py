# Python Project: CARD GAME

import random

# ------------------------
# Card class
# ------------------------
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def get_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11  # Initially counts as 11, can adjust later
        else:
            return int(self.value)

# ------------------------
# Deck class
# ------------------------
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# ------------------------
# Player class
# ------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = sum(card.get_value() for card in self.hand)

        aces = [card for card in self.hand if card.value == 'A']
        while value > 21 and aces:
            value -= 10
            aces.pop()
        return value
    
    def show_hand(self, reveal_all=True):
        if not reveal_all:
            print(f"{self.name} shows: {self.hand[0]} and a hidden card.")
        else:
            cards = ', '.join(str(card) for card in self.hand)
            print(f"{self.name} has: {cards} (Value: {self.get_hand_value()})")

# ------------------------
# BlackjackGame class
# ------------------------
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def start(self):
        print("=== Welcome to Blackjack! ===")
        # Deal two cards each
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        self.player.show_hand()
        self.dealer.show_hand(reveal_all=False)

        self.player_turn()
        self.dealer_turn()
        self.check_winner()

    def player_turn(self):
        while True:
            value = self.player.get_hand_value()
            if value > 21:
                print("You busted! You lose.")
                return
            choice = input("Do you want to hit (h) or stand (s)? ").lower()
            if choice == 'h':
                self.player.add_card(self.deck.deal_card())
                self.player.show_hand()
            elif choice == 's':
                break
            else:
                print("Invalid option. Choose 'h' or 's'.")

    def dealer_turn(self):
        print("\nDealer's turn...")
        self.dealer.show_hand()
        while self.dealer.get_hand_value() < 17:
            print("Dealer hits.")
            self.dealer.add_card(self.deck.deal_card())
            self.dealer.show_hand()
        if self.dealer.get_hand_value() > 21:
            print("Dealer busted! You win!")

    def check_winner(self):
        player_val = self.player.get_hand_value()
        dealer_val = self.dealer.get_hand_value()

        print("\n=== Final Results ===")
        self.player.show_hand()
        self.dealer.show_hand()

        if player_val > 21:
            print("You lost.")
        elif dealer_val > 21 or player_val > dealer_val:
            print("You win!")
        elif player_val < dealer_val:
            print("You lost.")
        else:
            print("It's a tie.")

# ------------------------
# Run the game
# ------------------------
if __name__ == "__main__":
    game = BlackjackGame()
    game.start()
