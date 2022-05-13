from abstract_storage import AbstractStorage
import sqlite3


class SQLiteStorage(AbstractStorage):

    def close_connection(self, conn):
        conn.close()

    def get_connection(self):
        conn = sqlite3.connect('./banking.db')
        return conn

    def insert_mock_data(self, conn):
        conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
        conn.commit()

