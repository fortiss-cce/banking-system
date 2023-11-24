from typing import List
from domain.bank_system import BankSystem
from domain.user import User


class BankSystemSQLite(BankSystem):
    def __init__(self, users: List[User] = ...) -> None:
        super().__init__(users)

    def import_users(filepath) -> None:
        pass

    def save_users(filepath) -> None:
        pass

    # def import_users_by_postgresql(self, filepath) -> None:
    #     pass

    def import_users_as_sqlite(self, filepath) -> None:
        pass

    def save_users_as_sqlite(self, filepath) -> None:
        pass

    def update(self, user:User) -> None:
        pass

