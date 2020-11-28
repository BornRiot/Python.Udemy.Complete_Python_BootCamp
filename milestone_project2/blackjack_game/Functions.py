"""
This module will be used to code the functions that are necessary for execution of the game that could not
be coded to specific classes.
"""


def hit(deck, hand):
    """
    Function to deal another card to the player or dealer
    """
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def take_bets(chips):
    chips.bet = int(input("Player, please enter a bet amount: "))
    if chips.bet > chips.total:
        print("Bet Exceeds Bankroll")
        print("Player Bet:", chips.bet, "Player Bankroll:", chips.total)
        exit(0)
    else:
        print("Player has placed a bet in the amount of: ", chips.bet)


def show_some(player, dealer):
    print("Player is currently showing: ")
    for card in player.cards:
        print(card)
    print("For a total value of: {h_value}".format(h_value=player.value))
    print("Dealer is showing: ")
    print("<Hidden Card>")
    print(dealer.cards[1])


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


#  Functions used to handle after game endings of either player or dealer winning or a push
def player_busts(player_hand, dealer_hand, chips):
    print("Player has busted.")
    chips.lose_bet()


def player_wins(player_hand, dealer_hand, chips):
    print("Dealer has busted.")
    chips.lose_bet()


def dealer_wins(player_hand, dealer_hand, chips):
    print("Player has busted.")
    chips.lose_bet()


def dealer_busts(player_hand, dealer_hand, chips):
    print("Dealer has busted.")
    chips.win_bet()


def push(player, dealer):
    print("Game has resulted in a push. Neither Player or Dealer (Won/Lost)")
    print("Bet has been returned ")
