from domain.account import Account


class User:

    _accounts: list[Account]
    name: str

    def __init__(self, name, accounts):
        self.name = name
        self._accounts = accounts
