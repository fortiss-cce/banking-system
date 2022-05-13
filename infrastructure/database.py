from abc import ABC, abstractmethod
from domain.user import User


class Database(ABC):
    @abstractmethod
    def __init__(file_path: str):
        pass

    @abstractmethod
    def addUser(self, user: User, balance: float):
        pass

    @abstractmethod
    def subtractMoneyFromUser(self, user: User, amount: float):
        pass

    @abstractmethod
    def addMoneyToUser(self, user: User, amount: float):
        pass

    @abstractmethod
    def printBalances(self, print_message: str):
        pass
