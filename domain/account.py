from domain.balance import Balance
from domain.history import History


class Account:

    balance: Balance
    history: History

    def __init__(self, balance, history):
        self.balance = balance
        self.history = history