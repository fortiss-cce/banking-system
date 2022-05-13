import sqlite3

from database import Database

from domain.user import User


class SQLDatabase(Database):
    def __init__(self, file_path: str) -> None:
        self.path = file_path
        self.connect()
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);"
        )
        self.conn.commit()
        self.closeDatabase()

    def connect(self):
        self.conn = sqlite3.connect(self.file_path)

    def closeDatabase(self):
        self.conn.close()

    def addUser(self, user: User, balance: float):
        self.connect()
        self.conn.execute(
            f"INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ({user.getName()}, {balance} )"
        )
        self.conn.commit()
        self.closeDatabase()

    def addMoneyToUser(self, user: User, amount: float):
        self.connect()
        cursor = self.conn.execute(
            "SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user.getName(),)
        )
        balance1 = 0
        for row in cursor:
            balance1 = row[0]
        self.conn.execute(
            "UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;",
            (
                (balance1 - amount),
                user.getName(),
            ),
        )
        self.closeDatabase()

    def subtractMoneyFromUser(self, user: User, amount: float):
        self.connect()
        cursor = self.conn.execute(
            "SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user.getName(),)
        )
        balance2 = 0
        for row in cursor:
            balance2 = row[0]
        self.conn.execute(
            "UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;",
            (
                (balance2 + amount),
                user.getName(),
            ),
        )

        self.conn.commit()
        self.closeDatabase()

    def printBalances(self, print_message: str):
        self.connect()
        cursor = self.conn.execute("SELECT * from ACCOUNT;")

        cursor = self.conn.execute("SELECT * from ACCOUNT;")
        print(f"\n{print_message}")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        self.closeDatabase()
