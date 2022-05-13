from abc import ABC
from domain.user import User


class Database(ABC):
    def __init__(file_path: str):
        pass

    def addUser(self, user: User, balance: float):
        pass

    def subtractMoneyFromUser(self, user: User, amount: float):
        pass

    def addMoneyToUser(self, user: User, amount: float):
        pass

    def printBalances(self, print_message: str):
        pass
