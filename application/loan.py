from domain.user import User


class Loan:
    def __init__(self, user:User) -> None:
        self._user = user

    def loan(self, user:User, money:float) -> User:
        pass

