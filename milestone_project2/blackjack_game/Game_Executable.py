"""
This module will be used to carry out the execution of the game by combining all the
other game objects to carry out the process of playing the
"""
# Import the necessary classes to carry out the process of playing the game
from milestone_project2.blackjack_game.Hand import *
from milestone_project2.blackjack_game.Chips import *


# Create the necessary game object to play the game
game_deck = Deck()
game_player = Hand()
game_chips = Chips()
print(game_chips.bet)
game_chips.take_bets()