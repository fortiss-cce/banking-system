from repository import AbstractRepository
from domain.user_account import UserAccount
from sqlite3 import Connection


class SQLiteRepository(AbstractRepository):

    def __init__(self, connection: Connection):
        self.connection = connection

    def get_user_account_by_name(self, name: str) -> UserAccount:
        cursor = self.connection.cursor()
        self.connection.execute("SELECT * from ACCOUNT WHERE NAME = ?;", (name,))
        res = cursor.fetchone()
        return UserAccount(*res)

    def update_account_balance_by_name(self, user_account: UserAccount, new_balance: float):
        self.connection.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (new_balance, user_account.name))
        self.connection.commit()

    def get_account_balance(self, user_account: UserAccount):
        cursor = self.connection.cursor()
        self.connection.execute("SELECT balance from ACCOUNT WHERE NAME = ?;", (user_account.name,))
        return cursor.fetchone()
