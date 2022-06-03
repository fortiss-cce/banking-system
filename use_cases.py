from entity import User
from database import SQLHandler


class DonateService:
    def donate(self, from_user: User, to_user: User, amount: float):
        sqlhandler = SQLHandler()
        balance_from = sqlhandler.get_balance_from_user(from_user)
        new_balance = balance_from - amount
        sqlhandler.set_balance_for_user(from_user, new_balance)

        balance_to = sqlhandler.get_balance_from_user(to_user)
        new_balance = balance_to + amount
        sqlhandler.set_balance_for_user(from_user, new_balance)
        sqlhandler.close_connection()


class WithdrawService:
    def transfer_amount(self, user: User, amount: float):
        sqlhandler = SQLHandler()
        balance_to = sqlhandler.get_balance_from_user(user)
        new_balance = balance_to - amount
        sqlhandler.set_balance_for_user(user, new_balance)
        sqlhandler.close_connection()


class PrintAllService():
    def printAllUsers(self, text: str):
        sqlhandler = SQLHandler()
        users = sqlhandler.get_all_user()
        print(text)
        for user in users:
            print("NAME = ", user.name, ";\tBALANCE = ", user.balance)
        sqlhandler.close_connection()


class GetUser:
    def get_user(self, user: str):
        sqlhandler = SQLHandler()
        return sqlhandler.get_user(user)
