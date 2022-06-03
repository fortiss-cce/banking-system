import sqlite3
from bank_domain import Account, AccountStore
from decimal import *

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
    def _get_account_balance(cursor: sqlite3.Cursor, acc: str) -> Decimal:
        cursor.execute(f"SELECT BALANCE FROM ACCOUNT WHERE NAME = '{acc}'");
        row = cursor.fetchone()
        if row is None:
            cursor.execute("ROLLBACK;")
            raise ValueError(f"invalid account: '{acc}'")
        return Decimal(row[0])

    def transfer_money(self, source: str, target: str, amount: Decimal) -> tuple[Account, Account]:
        cursor = self.connection.cursor()
        cursor.execute("BEGIN;")
        source_balance = SQLiteStore._get_account_balance(cursor, source)
        target_balance = SQLiteStore._get_account_balance(cursor, target)
        if source_balance < amount:
            cursor.close()
            raise ValueError(f"insufficient funds in account: '{source}' {source_balance}")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE - {amount} WHERE NAME = '{source}';")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE + {amount} WHERE NAME = '{target}';")
        self.connection.commit()
        cursor.close()
        return Account(source, source_balance - amount), Account(target, target_balance + amount)

    def withdraw_money(self, source: str, amount: Decimal) -> Account:
        cursor = self.connection.cursor()
        cursor.execute("BEGIN")
        source_balance = SQLiteStore._get_account_balance(cursor, source)
        if source_balance < amount:
            cursor.close()
            raise ValueError(f"insufficient funds in account: '{source}' {source_balance}")
        cursor.execute(f"UPDATE ACCOUNT SET BALANCE = BALANCE - {amount} WHERE NAME = '{source}';")
        self.connection.commit()
        cursor.close()
        return Account(source, source_balance - amount)

    def retreive_accounts(self) -> list[Account]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ACCOUNT")
        rows = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        accounts = []
        for row in rows:
            accounts.append(Account(row[0], Decimal(row[1])))
        return accounts