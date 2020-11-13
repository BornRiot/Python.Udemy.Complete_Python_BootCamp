"""
This module will be ued for the Hand class of the game and hold the carious methods and vasriables
needed to carry out the sewuence of game events.
"""
from milestone_project2.blackjack_game.Deck import *
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0




    def add_cards(self, card):
        if type(card) == type([]):
            # Get a list of multi card objects
            self.cards.extend(card)
        else:
            self.cards.append(card)

    def adjust_for_ace(self): # Function needs to be improved
        for card in self.cards:
            self.value += card.value
            if "Ace" in card.rank:
                return self.cards.index(card,0,)
    def get_values(self):
        for card  in self.cards:
            self.value += card.value







    def __str__(self):
        return f'Hand {self.name} has {len(self.all_cards)} cards and {self.bankroll} in his bankroll.'


the_deck = Deck()
the_deck.shuffle()
drawn_card = the_deck.deal_one()
drawn_card2  = the_deck.deal_one()

player_hand = Hand()
player_hand.add_cards([drawn_card, drawn_card2])
for card in player_hand.cards:
    print(card.rank, card.value)
player_hand.get_values()
print(player_hand.value)