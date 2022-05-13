import abc

from utilities import MoneyTransfer


class DataStorage:
    pass


class Broker(abc.ABC):

    storage: DataStorage

    def __init__(self, storage: DataStorage):
        self.storage = storage
        self.storage.initialize()

    @abc.abstractmethod
    def user_balance(self, user: str) -> float:
        """Returns the balance of the user's account."""

    @abc.abstractmethod
    def deposit(self, to_user: str, amount: float) -> None:
        """Deposits the amount to the to_user's account."""

    @abc.abstractmethod
    def withdraw(self, from_user: str, to_user: str, amount: float) -> None:
        """Withdraws the amount from the from_user's account to the to_user's account."""

    @abc.abstractmethod
    def transfer(self, transfer: MoneyTransfer) -> None:
        """Transfers the amount from the from_user's account to the to_user's account."""
        assert self.withdraw(transfer.from_user, transfer.amount) == transfer.amount
        assert self.deposit(transfer.to_user, transfer.amount) == transfer.amount


class SqlBroker(Broker):

    def user_balance(self, user: str) -> float:
        return self.storage.execute(f"SELECT balance FROM users WHERE name = '{user}'")

    def deposit(self, to_user: str, amount: float) -> None:
        self.storage.execute(f"UPDATE users SET balance = balance + {amount} WHERE name = '{to_user}'")

    def withdraw(self, from_user: str, amount: float) -> None:
        self.storage.execute(f"UPDATE users SET balance = balance - {amount} WHERE name = '{from_user}'")
