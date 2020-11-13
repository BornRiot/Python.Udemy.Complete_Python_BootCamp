"""
This module will be used to create the Chips class for the game. Ut hold the necessary methods to carry
the betting, holding and rewarding of chips to  the player or dealer after each round or hand is played
"""


# Explanation of class vs. instances variables: https://do.co/3p27Bip
# Vide Explanation of class vs instance variables: https://bit.ly/38n2VgY
# https://bit.ly/32FpZnN
# https://bit.ly/3p9q10r


class Chips:
    def __init__(self):
        # Hand Bankroll and Bet
        self.total = int(input("Please enter buy-in amount for table: "))
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

    def take_bets(self):
        self.bet = int(input("Hand, please enter a bet amount: "))
        if self.bet > self.total:
            print("Bet Exceeds Bankroll")
            print("Hand Bet:", self.bet, "Hand Bankroll:", self.total)
            exit(0)
        else:
            print("Hand has placed a bet in the amount of: ", self.bet)


new_chip = Chips()
new_chip.take_bets()
new_chip.lose_bet()
print(new_chip.total)
