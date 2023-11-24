from os import statvfs
import sqlite3

from user import User

class DataBase():

    _conn = sqlite3.connect("./banking.db")

    @staticmethod
    def setup():
        DataBase._conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        DataBase._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        DataBase._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        DataBase._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        DataBase._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Alexandros', 1.00 )")
        DataBase._conn.commit()

    @staticmethod
    def _get_balance(name):
        cursor = DataBase._conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (name))
        balance = 0
        for row in cursor:
            balance = row[0]
        return balance

    @staticmethod
    def get_user(name):
        balance = DataBase._get_balance(name)
        return User(name, balance)

    @staticmethod
    def update_user(user):
        DataBase._conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (user._balance, user._uid,))

    @staticmethod
    def teardown():
        DataBase._conn.close()
