from abc import ABC, abstractmethod
from typing import Iterable

from domain.account import Account

class StorageTransaction(ABC):

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, type, value, traceback):
        pass

    @abstractmethod
    def updateAccountBalance(self, account: Account, amount: float):
        pass

class Storage(ABC):

    @abstractmethod
    def transaction(self) -> StorageTransaction:
        pass

    @abstractmethod
    def getAllAccounts(self) -> Iterable[Account]:
        pass

    @abstractmethod
    def getAccountForName(self, name: str) -> Account:
        pass


