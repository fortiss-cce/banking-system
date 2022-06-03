from bank_domain import AccountStore, Account

class BankService:
    store: AccountStore

    def __init__(self, store: AccountStore):
        self.store = store

    def prepare(self):
        self.store.prepare()
    def create_account(self, account: Account):
        self.store.create_account(account)
    def retreive_accounts(self) -> list[Account]:
        return self.store.retreive_accounts()
    def transfer_money(self, source: Account, target: Account, amount: float) -> tuple[Account, Account]:
        return self.store.transfer_money(source, target, amount)
    def withdraw_money(self, source: Account, target: Account, amount: float) -> tuple[Account, Account]:
        return self.store.withdraw_money(source, amount)
