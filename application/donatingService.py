class DonatingService:

    def __init__(self):
        return self

    def donate_from_user1_to_user2(self, repository: Repository, user1: User, user2: User, amount: float):
        balance_1 = repository.getBalance(user=user1)
        balance_2 = repository.getBalance(user=user2)
        new_balance1 = balance_1 - amount
        new_balance2 = balance_1 + amount
        repository.updateBankAccount(user=user1, new_balance=new_balance1)
        repository.updateBankAccount(user=user2, new_balance=new_balance2)