from user import User

class BankAccount:
    _balance: float
    _user: User
    def __init__(self, user: User):
        self._balance = 0
        self._user = user
    def getBalance(self):
        return self._balance
    def setBalance(self, new_balance: float):
        self._balance = new_balance
    def getUser(self):
        return self._user