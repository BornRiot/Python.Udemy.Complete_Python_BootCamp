from Deck import *


class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # Get a list of multi card objects
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards and {self.bankroll} in his bankroll.'
the_deck = Deck()
print(the_deck.all_cards)
first_card = the_deck.all_cards[4]
print(first_card)
the_player = Player("Michael", 10000)
print(the_player.all_cards)