from dataclasses import dataclass

from application import Storage


@dataclass
class DonateService():
    storage: Storage
    
    def donate(self, from_user: str, to_user: str, amount: float) -> None:
        from_account = self.storage.getAccountForName(from_user)
        to_account = self.storage.getAccountForName(to_user)

        with self.storage.transaction() as transaction:

            transaction.updateAccountBalance(from_account, from_account.balance - amount)

            transaction.updateAccountBalance(to_account, to_account.balance + amount)
