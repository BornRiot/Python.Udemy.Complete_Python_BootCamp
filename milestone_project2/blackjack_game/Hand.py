"""
This module will be ued for the Hand class of the game and hold the carious methods and vasriables
needed to carry out the sewuence of game events.
"""
from milestone_project2.blackjack_game.Deck import *
from milestone_project2.blackjack_game.Card import *

class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        # Code Implementation solves the issue with
        # adjusting for aces and calculating card values in hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1







the_deck = Deck()
the_deck.shuffle()
drawn_card = the_deck.deal_one()
drawn_card2  = the_deck.deal_one()

player_hand = Hand()
player_hand.add_card(drawn_card)
player_hand.add_card(drawn_card2)
print(drawn_card.rank)

