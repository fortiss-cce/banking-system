from abc import ABC, abstractmethod
from typing import Iterable

from domain.account import Account


class Storage(ABC):

    @abstractmethod
    def updateAccountBalance(account: Account, amount: float):
        pass

    @abstractmethod
    def getAllAccounts() -> Iterable[Account]:
        pass

    @abstractmethod
    def getAccountForName(name: str) -> Account:
        pass