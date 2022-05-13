# Copyright (C) 2022 RostLab
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from pathlib import Path
import sqlite3
from unicodedata import name

from requests import patch

from ..domain.data import DataStore

from ..domain.core import (
    IncomingTransaction,
    OutgoingTransaction,
    Transaction,
    Account,
)


class SQLiteStore(DataStore):
    def __init__(self, path: Path = Path("./banking.db")) -> None:
        super().__init__()
        self.path = path

    # NOTE: cursor needs a proper type; just too lazy rn
    def _handle_incoming_transaction(transaction: IncomingTransaction, cursor: object):
        pass

    def _handle_outgoing_transaction(transaction: OutgoingTransaction, cursor: object):
        pass

    def setup(self):
        self.conn = sqlite3.connect(self.path.to_absolute())
        self.conn.isolation_level = None

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);"
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );"
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )"
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )"
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )"
        )
        self.conn.commit()

    def execute_transactions(self, transactions: list[Transaction]):

        db_cursor = self.conn.cursor()
        db_cursor.execute("begin")
        try:
            for transaction in transactions:
                if type(transaction) is OutgoingTransaction:
                    self._handle_outgoing_transaction(transaction)
                elif type(transaction) is IncomingTransaction:
                    self._handle_incoming_transaction(transaction)
                else:
                    raise ValueError(f"Unknown transaction type {type(transaction)}!")

        except self.conn.Error as error:
            db_cursor.execute("rollback")
            raise error

    def get_account_info(self) -> list[Account]:
        accounts = list()
        with self.conn.execute("SELECT * from ACCOUNT;") as cursor:
            for row in cursor:
                account = Account(name=row[0], balance=float(row[1]))
                accounts.append(account)
        return accounts

    def get_account_for_username(self, name: str) -> Account:
        return Account("", 4)

    def teardown(self):
        self.conn.close()
