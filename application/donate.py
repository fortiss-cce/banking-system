from domain.account import Account
from domain.balance_change import BalanceChange

class Donate(BalanceChange):

    donate_to_account: Account

    def __init__(self, donate_to_account):
        self.donate_to_account = donate_to_account

    def calculate_new_balance(self):
        self.account.balance -= self.amount_of_change
        self.donate_to_account += self.donate_to_account


