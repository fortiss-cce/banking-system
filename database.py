import sqlite3
from entity import User


class SQLHandler:
    def __init__(self):
        self.conn = sqlite3.connect('./banking.db')

    def init_test_clients(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
        self.conn.commit()

    def get_balance_from_user(self, user: User):
        cursor = self.conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user.name,))
        balance = 0
        for row in cursor:
            balance = row[0]
        return balance

    def set_balance_for_user(self, user: User, target_balance: float):
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;",
                     ((target_balance), user.name,))
        self.conn.commit()

    def get_user(self, user: str):
        cursor = self.conn.execute("SELECT * from ACCOUNT WHERE NAME = ?;", (user))
        user = [User(row[0], row[1]) for row in cursor]
        return user[0]

    def get_all_user(self):
        cursor = self.conn.execute("SELECT * from ACCOUNT;")
        all_users = [User(row[0], row[1]) for row in cursor]
        return all_users

    def close_connection(self):
        self.conn.close()
