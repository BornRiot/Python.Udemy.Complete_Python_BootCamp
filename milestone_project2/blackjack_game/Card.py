"""
This module is used to create the Card  class fir all 52 cards the will be used in the simulation
of the Blackjack game.
"""

# Creation of the card class should include the following properties: Suit, Rank, Value
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 9, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': {'One': 1, 'Eleven': 11}}
# {'One': 1, 'Eleven': 11} Temporarily commented out
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


