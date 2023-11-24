from domain.repository import Repository
from domain.user import User

class WithdrawingService:

    def __init__(self):
        return self

    def withdraw_from_user(self, repository: Repository, user: User, amount: float):
        balance = repository.getBalance(user=user)
        new_balance = balance - amount
        repository.updateBankAccount(user=user, new_balance=new_balance)