from repositories.sqlite_repository import SQLiteRepository


class UserAccountService:

    def __init__(self, connection):
        self.repository = SQLiteRepository(connection)

    def withdraw(self, user, amount):
        user_account = self.repository.get_user_account_by_name(user)
        self.repository.update_account_balance_by_name(user_account, amount)

    def donate(self, from_user, to_user, amount):
        from_user_account = self.repository.get_user_account_by_name(from_user)
        to_user_account = self.repository.get_user_account_by_name(to_user)
        self.repository.update_account_balance_by_name(from_user, from_user_account.balance - amount)
        self.repository.update_account_balance_by_name(to_user_account, to_user.balance + amount)
