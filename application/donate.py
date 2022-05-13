from abc import ABC, abstractmethod
from domain.user import User


class DonationService(ABC):
    @abstractmethod
    def donate(self, from_user: User, to_user: User, amount: float):
        pass
