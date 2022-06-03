class Account:
    name: str
    balance: float

    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

class AccountStore:
    def prepare(self):
        pass 
    def create_account(self):
        pass
    def transfer_money(self, source: Account, target: Account, amount: float):
        pass
    def withdraw_money(self, source: Account, amount: float):
        pass
    def retreive_accounts(self) -> list[Account]:
        pass
