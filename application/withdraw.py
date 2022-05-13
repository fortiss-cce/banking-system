from abc import ABC, abstractmethod
from domain.user import User


class WithdrawService(ABC):
    @abstractmethod
    def withdraw(from_user: User, amount: float):
        pass
