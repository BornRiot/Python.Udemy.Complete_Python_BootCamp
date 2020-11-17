"""
This module will be used to carry out the execution of the game by combining all the
other game objects to carry out the process of playing the
"""
# Import the necessary classes to carry out the process of playing the game
from milestone_project2.blackjack_game.Hand import *
from milestone_project2.blackjack_game.Chips import *


def hit(deck, hand):
    """
    Function to deal another card to the player or dealer
    """
    dealt_card = deck.deal_one()
    print("The dealt card: {the_card}  was added to {name} hand".format(the_card=dealt_card, name=hand.name))
    hand.add_card(dealt_card)


def hit_or_stand(deck, hand):
    """Function  for hitting(Taking another card from the deck) or standing(staying with t
    he cards that are already in hand"""
    global playing
    response = input("Would you like to hit or stand?: ")
    response = response.lower()
    if response == "hit":
        playing = True
        hit(deck, hand)
    elif response == "stand":
        playing = False
        print("Player is standing with the cards currently in hand")


def show_some(player, dealer):
    print(player.cards[0])


# Create the necessary game objects to test the game
playing = False

game_chips = Chips()
game_deck = Deck()
game_deck.shuffle()
player_hand = Hand("Mike")
dealer_hand = Hand("Dealer 1")
first_card = game_deck.deal_one()
print(first_card)
first_card = game_deck.deal_one()
print(first_card)
first_card = game_deck.deal_one()
print(first_card)

player_hand.add_card(first_card)
player_hand.add_card(first_card)
player_hand.add_card(first_card)

hit_or_stand(game_deck, player_hand)
show_some(player_hand, dealer_hand)
