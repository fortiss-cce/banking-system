
from application.utils import print_balances


@dataclass
class Withdraw():
    
    def withdraw(self, user: str, amount: float):
        # user = args["<user>"]
        # amount = float(args["<amount>"])

        print_balances(self.storage, "Before")

        cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user,))
        balance = 0
        for row in cursor:
            balance = row[0]
        conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance - amount), user,))

        conn.commit()

        print_balances(self.storage, "After")

        conn.close()
