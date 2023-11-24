from domain.balance import Balance
from domain.history import History


class Account:

    account_id: int
    balance: Balance
    history: History

    def __init__(self, account_id, balance, history):

        self.account_id = account_id
        self.balance = balance
        self.history = history
