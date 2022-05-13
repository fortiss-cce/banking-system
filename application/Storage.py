from abc import ABC, abstractmethod
from typing import Iterable

from domain.account import Account


class Storage(ABC):

    @abstractmethod
    def updateAccountBalance(self, account: Account, amount: float):
        pass

    @abstractmethod
    def getAllAccounts(self) -> Iterable[Account]:
        pass

    @abstractmethod
    def getAccountForName(self, name: str) -> Account:
        pass