from domain.user import User
from domain.bank_system import BankSystem


class Donation:
    def __init__(self, user:User) -> None:
        self._user = user

    def donate(self, user:User, money:float) -> User:
        pass


