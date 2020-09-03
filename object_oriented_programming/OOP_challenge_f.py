"""
OOP Challenge
"""

class BankAccount:
    balance = 0
    owner = ""

    def __init__(self, f_name, l_name, opening_balance):
        self.l_name = l_name
        self.f_name = f_name
        self.opening_balance = opening_balance
        # Return bank balance and owner info
        self.balance += opening_balance
        self.owner = self.f_name + " " + self.l_name

    def deposit(self, amount):
        if amount <= 0:
            try:
                raise ValueError
            except ValueError:
                print("Deposit amount is less than or equal to 0")
        else:
            self.balance += amount
            print("The current balance after depositing  {deposit_amt} is: {new_amt}"
                  .format(deposit_amt=amount, new_amt=self.balance))

    def withdrawal(self, amount):
        if amount > self.balance:
            try:
                raise ValueError
            except ValueError:
                print("Withdrawal amount exceeds current bank balance")
        else:
            self.balance -= amount
            print("The current balance after withdrawing {withdraw_amt} is: {new_amt}"
                  .format(withdraw_amt=amount, new_amt=self.balance))


bank1 = BankAccount("Marvin", "DaCosta", 5000)
print(bank1.owner)
print(bank1.balance)

bank1.deposit(100)
bank1.deposit(-122)
bank1.withdrawal(250)
bank1.withdrawal(290000)
print(bank1.balance)

