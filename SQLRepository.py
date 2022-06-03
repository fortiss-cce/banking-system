from Repository import Repository
import sqlite3

class SQLRepository(Repository):

    def __init__(self, filename: str):
        self.conn = sqlite3.connect(filename)
        self.create()

    def create(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
        self.conn.commit()

    def get_full_data(self):
        return self.conn.execute("SELECT * from ACCOUNT;")

    def get_balance(self, user: str):
        return self.conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user,))

    def update_balance(self, amount: float, user: str):
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (amount, user,))

    def update(self):
        self.conn.commit()

    def disconnect(self):
        self.conn.close()

    def print_all(self):
        cursor = self.get_full_data()
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])
