from dataclasses import dataclass

from application import Storage
from application.utils import print_balances


@dataclass
class DonateService():
    storage: Storage
    
    def donate(self, from_user: str, to_user: str, amount: float) -> None:

        #with self.storage.transation() as transaction:
        #    pass
            from_account = self.storage.getAccountForName(from_user)
            to_account = self.storage.getAccountForName(to_user)

            self.storage.updateAccountBalance(from_account, from_account.balance - amount)

            self.storage.updateAccountBalance(to_account, to_account.balance + amount)
