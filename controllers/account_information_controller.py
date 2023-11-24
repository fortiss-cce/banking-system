class AccountInformationController:

    def __init__(self, account):
        self.account = account

    def get_account_id(self) -> int:
        return self.account.id

    def get_account_balance(self) -> float:
        return self.account.balance
