from domain.balance_change import BalanceChange


class Withdraw(BalanceChange):

    def __init__(self):
        pass
    def calculate_new_balance(self):
        self.account.balance += self.amount_of_change