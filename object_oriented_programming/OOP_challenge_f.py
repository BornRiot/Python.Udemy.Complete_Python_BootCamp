"""
For this challenge, create a bank account class that has two attributes:
owner
balance
and two methods:
deposit
withdraw
"""


class BankAccount:
    balance = 0
    owner = ""

    def __init__(self, f_name, l_name):
        self.l_name = l_name
        self.f_name = f_name


bank1 = BankAccount("Marvin", "DaCosta")
bank1.owner = bank1.f_name + " " + bank1.l_name
print(bank1.owner)
