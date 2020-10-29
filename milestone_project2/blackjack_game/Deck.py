# New Lecture topic starts here: Creating Deck Class
# Vide Demonstrates how to create the deck class for the game War in python
# Look into a possible shuffle package in java
from Card import *
import random


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


