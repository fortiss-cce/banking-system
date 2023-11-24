from domain.user import User


class Withdraw:
    def __init__(self, user:User) -> None:
        self._user = user

    def withdraw(self, money:float) -> User:
        pass

