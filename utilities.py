from typing import NamedTuple


class MoneyTransfer(NamedTuple):
    from_user: str
    to_user: str
    amount: float


DEMO_DB_SETUP = (
    "CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);",
    "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );",
    "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )",
    "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )",
    "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
STORAGE_PATH = './banking.db'
