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
    global dealt_card
    dealt_card = deck.deal_one()
    if "Dealer" not in hand.name:
        print("The dealt card: {the_card}  was added to {name} hand".format(the_card=dealt_card, name=hand.name))
    hand.add_card(dealt_card)


def hit_or_stand(deck, hand):
    """Function  for hitting(Taking another card from the deck) or standing(staying with t
    he cards that are already in hand"""
    global playing
    name = hand.name

    if "Dealer" not in name:
        print("{the_name} would you like to hit or stand:".format(the_name=name))
        response = input()
        response = response.lower()
        if response == "hit":
            playing = True
            hit(deck, hand)
        elif response == "stand":
            playing = False
            print("Player is standing with the cards currently in hand")
    elif "Dealer" in name and hand.value < 17:
        playing = True
        hit(deck, hand)
    #  Function needs to be improved to automatically hit or stand for dealers hand


def show_some(player, dealer):
    print("{player_name} is showing: ".format(player_name=player.name))
    for card in range(len(player.cards)):
        print(player.cards[card])
    print("For a total value of: ", player.value)
    print(" ")
    print("{dealer_name} is showing".format(dealer_name=dealer_hand.name))
    for card in range(len(dealer.cards)):
        print(dealer.cards[0])
    print("For a total value of: ", dealer.value)


def show_all(player, dealer):
    print("The player is showing: ")
    for card in range(len(player.cards)):
        print(player.cards[card])
    print("For a total value of: ", player.value)
    print(" ")
    print("The Dealer is showing: ")
    for card in range(len(dealer.cards)):
        print(dealer.cards[card])
    print("For a total value of: ", dealer.value)


def player_busts():
    p_val = player_hand.value
    d_val = dealer_hand.value
    if p_val < d_val:
        print("Player value: ", p_val)
    else:
        print("Dealer value: ", d_val)


def player_wins():
    pass


def dealer_wins():
    pass


def dealer_busts():
    pass


def push():
    pass


# Create the necessary game objects to test the game
playing = False

game_chips = Chips()
game_deck = Deck()
game_deck.shuffle()
player_hand = Hand("Mike")
dealer_hand = Hand("Dealer 1")

# Deal player a card
dealt_card = game_deck.deal_one()
player_hand.add_card(dealt_card)

del dealt_card
dealt_card = game_deck.deal_one()
player_hand.add_card(dealt_card)

# Deal the dealer a card
dealt_card = game_deck.deal_one()
del dealt_card
dealt_card = game_deck.deal_one()

dealer_hand.add_card(dealt_card)
show_some(player_hand, dealer_hand)
# Ask if the players want to hit or stand:
hit_or_stand(game_deck, player_hand)
hit_or_stand(game_deck, dealer_hand)
show_some(player_hand, dealer_hand)
print("The line below shows all cards")
show_all(player_hand, dealer_hand)
player_busts()
