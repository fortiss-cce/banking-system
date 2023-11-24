from abc import abstractmethod

from domain.account import Account


class BalanceChange:

    account: Account
    amount_of_change: float

    def __init__(self, account, amount_of_change):
        self.account = account
        self.amount_of_change = amount_of_change

    @abstractmethod
    def calculate_new_balance(self):
        pass
