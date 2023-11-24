from domain.account import Account


class User:

    _accounts: list[Account]

    def __init__(self, accounts):
        self._accounts = accounts
