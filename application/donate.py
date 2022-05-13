from abc import ABC
from domain.user import User

class DonationService(ABC):
    def donate(self, from_user: User, to_user: User, amount:float):
        pass
