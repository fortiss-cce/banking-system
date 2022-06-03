import sqlite3
from docopt import docopt

__doc__ = """
Donation System
Usage:
    app.py list
    app.py transfer --from <from_user> --to <to_user> --amount <amount>
    app.py withdraw --user <user> --amount <amount>

Options:
    -f, --from             The user from which bank account is transferred.
    -t, --to               The user to which bank account is transferred.
    -u, --user             The user wanting to withdraw money from his/her account.
    -a, --amount           The amount handled by the command.
    
Existing accounts:
    * MagazinRoyale
    * FynnKliemann
    * Peter
    * Johannes
"""

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

class SQLiteStore(AccountStore):
    connection: sqlite3.Connection

    def __init__(self, path: str):
        super().__init__()
        self.connection = sqlite3.connect(path)
        self.connection.isolation_level = None

    def prepare(self):
        self.connection.executescript(f"""
            BEGIN;
            CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);
            COMMIT;
        """)

    def create_account(self, account: Account):
        self.connection.executescript(f"""
            BEGIN;
            INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('{account.name}', {account.balance});
            COMMIT;
        """);

    @staticmethod
    def _get_account_balance(cursor: sqlite3.Cursor, acc: str) -> float:
        cursor.execute(f"SELECT BALANCE FROM ACCOUNT WHERE NAME = '{acc}'");
        row = cursor.fetchone()
        if row is None:
            cursor.execute("ROLLBACK;")
            raise ValueError(f"invalid account: '{acc}'")
        return float(row[0])

    def transfer_money(self, source: str, target: str, amount: float) -> tuple[Account, Account]:
        cursor = self.connection.cursor()
        cursor.execute("BEGIN;")
        source_balance = SQLiteStore._get_account_balance(cursor, source)
        target_balance = SQLiteStore._get_account_balance(cursor, target)
        if source_balance < amount:
            cursor.close()
            raise ValueError(f"insufficient funds in account: '{source}' {source_balance}")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE - {amount} WHERE NAME = '{source}';")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE + {amount} WHERE NAME = '{target}';")
        cursor.execute("COMMIT;")
        cursor.close()
        return Account(source, source_balance - amount), Account(target, target_balance + amount)

    def withdraw_money(self, source: str, amount: float) -> Account:
        cursor = self.connection.cursor()
        cursor.execute("BEGIN")
        source_balance = SQLiteStore._get_account_balance(cursor, source)
        if source_balance < amount:
            cursor.close()
            raise ValueError(f"insufficient funds in account: '{source}' {source_balance}")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE - {amount} WHERE NAME = '{source}';")
        cursor.close()
        return Account(source, source_balance - amount)

    def retreive_accounts(self) -> list[Account]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ACCOUNT")
        rows = cursor.fetchall()
        cursor.close()
        accounts = []
        for row in rows:
            accounts.append(Account(row[0], float(row[1])))
        return accounts

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

def setup_dummy_bank_service(bank: BankService):
    bank.create_account(Account('MagazinRoyale', 1000.00))
    bank.create_account(Account('FynnKliemann', 1000.00))
    bank.create_account(Account('Peter', 1000000.00))
    bank.create_account(Account('Johannes', 1.00))

if __name__ == '__main__':
    store = SQLiteStore('./banking.db')
    bank = BankService(store)
    bank.prepare()
    setup_dummy_bank_service(bank)

    args = docopt(__doc__)

    try:
        if args["transfer"]:
            from_user = args["<from_user>"]
            to_user = args["<to_user>"]
            amount = float(args["<amount>"])

            from_account, to_account = bank.transfer_money(from_user, to_user, amount)
            print(f"""Transferred money:
    {from_account.name.ljust(30)} {from_account.balance + amount} - {amount}
    {to_account.name.ljust(30)} {to_account.balance - amount} + {amount}
    """)

        elif args["withdraw"]:
            from_account = bank.withdraw_money(from_user, amount)
            print(f"""Withdrew money:
    {from_account.name.ljust(30)} {from_account.balance + amount} - {amount}
    """)

        elif args["list"]:
            accounts = bank.retreive_accounts()
            for account in accounts:
                print(f"{account.name.ljust(30)} {account.balance}")

    except ValueError as e:
        print(e)