from domain.account import Account
from abc import ABC, abstractmethod
from typing import Iterable


class Storage(ABC):
    
    @abstractmethod
    def updateAccountBalance(account: Account, amount: float):
        pass
    
    @abstractmethod
    def getAllAccounts() -> Iterable[Account]:
        pass
    
    @abstractmethod
    def getAccountForName(name: str) -> Account:
        pass


@dataclass
class Donate():
    storage: Storage
    
    def donate(self, from_user: str, to_user: str, amount: float) -> None:
        # from_user = args["<from_user>"]
        # to_user = args["<to_user>"]
        # amount = float(args["<amount>"])

        # 1. Status before exe
        
        #
        print_balances(conn, "Before")

        from_account = self.storage.getAccountForName(from_user)
        to_account = self.storage.getAccountForName(to_user)

        # cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (from_user,))

        # balance1 = 0
        # for row in cursor:
        #     balance1 = row[0]

        storage.updateAccountBalance(from_account, from_account.balance - amount)
        # conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance1 - amount), from_user,))

        # cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (to_user,))

        # balance2 = 0
        # for row in cursor:
        #     balance2 = row[0]

        storage.updateAccountBalance(to_account, to_account.balance + amount)
        # conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance2 + amount), to_user,))

        # conn.commit()
        print_balances(conn, "After")
        # conn.close()

    def print_balances(self, conn, time: str):
        accounts = self.storage.getAllAccounts()
        # cursor = conn.execute("SELECT * from ACCOUNT;")
        print(f"{time} donation:")
        for row in accounts:
            print("NAME = ", row.name, ";\tBALANCE = ", row.balance)
