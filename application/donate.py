from dataclasses import dataclass

from application import Storage


@dataclass
class Donate():
    storage: Storage
    
    def donate(self, from_user: str, to_user: str, amount: float) -> None:

        self.print_balances("Before")

        from_account = self.storage.getAccountForName(from_user)
        to_account = self.storage.getAccountForName(to_user)

        self.storage.updateAccountBalance(from_account, from_account.balance - amount)

        self.storage.updateAccountBalance(to_account, to_account.balance + amount)

        self.print_balances("After")

    def print_balances(self, conn, time: str):
        accounts = self.storage.getAllAccounts()
        print(f"{time} donation:")
        for row in accounts:
            print("NAME = ", row.name, ";\tBALANCE = ", row.balance)
