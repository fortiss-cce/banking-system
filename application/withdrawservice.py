from dataclasses import dataclass

from application.Storage import Storage
from application.utils import print_balances


@dataclass
class WithdrawService():
    storage: Storage

    def withdraw(self, user: str, amount: float):
        # user = args["<user>"]
        # amount = float(args["<amount>"])

        cursor = self.conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user,))
        balance = 0
        for row in cursor:
            balance = row[0]
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance - amount), user,))

        self.conn.commit()


        self.conn.close()
