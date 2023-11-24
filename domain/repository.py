from abc import ABC, abstractmethod
from bankaccount import BankAccount
from user import User

class Repository(ABC):
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def addBankAccount(self, BankAccount):
        pass
    
    @abstractmethod
    def getBankAccount(self, user: User):
        pass

    @abstractmethod
    def updateBankAccount(self, user: User, new_balance: float):
        pass

    @abstractmethod
    def getBalance(self, user: User):
        pass