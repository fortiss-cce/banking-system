import sqlite3
from sqlite3 import Connection
from typing import Iterable

from application.Storage import Storage
from domain.account import Account


class SQLStorage(Storage):

    conn: Connection

    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        print('Open Transaction')

    def __exit__(self):
        print('Close Transaction')

    def updateAccountBalance(self, account: Account, amount: float):
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (amount, account.name,))

    def getAllAccounts(self) -> Iterable[Account]:
        cursor = self.conn.execute("SELECT * from ACCOUNT;")
        return [Account(row[0], row[1]) for row in cursor]

    def getAccountForName(self, name: str) -> Account:
        cursor = self.conn.execute("SELECT NAME, BALANCE FROM ACCOUNT WHERE NAME = ?;", (name,))
        for row in cursor:
            return Account(row[0], row[1])
