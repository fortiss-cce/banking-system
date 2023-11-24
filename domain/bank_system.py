from domain.user import User
from typing import List

class BankSystem:
    def __init__(self, users:List[User]=[]) -> None:
        self.users = users

    def add_user(self, user:User) -> None:
        self.users.append(user)



