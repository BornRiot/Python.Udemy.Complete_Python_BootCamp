"""
This module will be used to simulate the Deck of cards that will be used in the game. \
The Deck consists of 52 cards with four different suits.
"""

import random # Look into a possible shuffle package in java
from milestone_project2.blackjack_game.Card import *
# Implementation of the Deck Class
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card objects

                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    # Create a method to deal one card from the deck of cards
    def deal_one(self):
        return self.all_cards.pop()


test_deck = Deck()
print(test_deck)