from abc import ABC
from domain.user import User


class WithdrawService(ABC):
    def withdraw(from_user: User, amount: float):
        pass
