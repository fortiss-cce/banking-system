import sqlite3
from sqlite3 import Connection
from typing import Iterable

from application.Storage import Storage, StorageTransaction
from domain.account import Account

class SQLStorageTransaction(StorageTransaction):
    conn: Connection
    sub_conn: Connection

    def __init__(self, conn: Connection):
        self.conn = conn

    def __enter__(self):
        self.sub_conn = self.conn.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        self.sub_conn.__exit__(type, value, traceback)

    def updateAccountBalance(self, account: Account, amount: float):
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (amount, account.name,))


class SQLStorage(Storage):

    conn: Connection

    def __init__(self, db: str):
        self.conn = sqlite3.connect(db, isolation_level=sqlite3.le)

    def transaction(self) -> StorageTransaction:
        return SQLStorageTransaction(self.conn)

    def getAllAccounts(self) -> Iterable[Account]:
        cursor = self.conn.execute("SELECT * from ACCOUNT;")
        return [Account(row[0], row[1]) for row in cursor]

    def getAccountForName(self, name: str) -> Account:
        cursor = self.conn.execute("SELECT NAME, BALANCE FROM ACCOUNT WHERE NAME = ?;", (name,))
        for row in cursor:
            return Account(row[0], row[1])
