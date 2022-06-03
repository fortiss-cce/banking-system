from multiprocessing.connection import Connection
import sqlite3
from domain.bank_repository import BankRepository
from domain.user import User


class SqlightRepository(BankRepository):

    conn: Connection

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('./banking.db')

        self.conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        self.conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
        self.conn.commit()

    def insert_user(self, user: User):
        self.conn.execute(f"INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ({user.get_name_of_user()}, {user.get_balance_of_user()})")

    def get_connection(self):
        return self.conn

    def get_user_by_name(self, user_name: str):
        return self.conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user_name,))

    def get_database(self):
        return self.conn.execute("SELECT * from ACCOUNT;")
        
    def get_balance(self, user_name:str):
        return self.conn.execute(f"SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user_name,))

    def update_account(self, user_name:str, balance:float):
        self.conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (balance, user_name,))

    def commit(self):
        self.conn.commit()

    def close_connection(self):
        self.conn.close()