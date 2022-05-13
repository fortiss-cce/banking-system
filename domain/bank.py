from domain.user import User
from application.donate import DonationService
from application.withdraw import WithdrawService
from infrastructure.database import Database


class Bank(DonationService, WithdrawService):
    def __init__(self, database) -> None:
        self.database: Database = database

    def donate(self, from_user: User, to_user: User, amount: float):
        self.database.printBalances("Before donation:")
        self.database.subtractMoneyFromUser(from_user, amount)
        self.database.addMoneyToUser(to_user, amount)
        self.database.printBalances("After donation:")

    def withdraw(self, from_user: User, amount: float):
        self.database.printBalances("Before withdrawal:")
        self.database.subtractMoneyFromUser(from_user, amount)
        self.database.printBalances("After withdrawal:")
