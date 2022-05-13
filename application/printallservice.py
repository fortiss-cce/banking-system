from dataclasses import dataclass

from application.Storage import Storage


@dataclass
class PrintAllAccountsService():
    storage: Storage

    def print_balances(self, time: str):
        accounts = self.storage.getAllAccounts()
        print(f"{time} donation:")
        for row in accounts:
            print("NAME = ", row.name, ";\tBALANCE = ", row.balance)
