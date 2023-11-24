import sqlite3

from cmd import CMDDonate, CMDWithdraw


class DataBase():

    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
        self._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
        self._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
        self._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
        self._conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Alexandros', 1.00 )")
        self._conn.commit()

    def _print_account_state(self, message):
        cursor = self._conn.execute("SELECT * from ACCOUNT;")
        print(message)
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

    def _remove_from_source(self, cmd, balance):
        next_balance = balance-cmd._amount
        if (next_balance < 0):
            raise AttributeError("Going in the RED!")
        self._conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", (next_balance, cmd._from_user,))

    def _add_to_destination(self, cmd):
        cursor = self._conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (cmd._to_user,))
        balance = 0
        for row in cursor:
            balance = row[0]
        self._conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance + cmd._amount), cmd._to_user,))

    def _get_balance(self, cmd):
        cursor = self._conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (cmd._to_user,))
        balance = 0
        for row in cursor:
            balance = row[0]
        return balance

    # TODO: each section of the next method could be a method
    def _execute_donate_cmd(self, cmd): 
        self._print_account_state("Before donation:")
        balance = self._get_balance(cmd)
        self._remove_from_source(cmd, balance)
        self._add_to_destination(cmd)
        self._conn.commit() # was missing in previous version: normal??

    def _execute_withdraw_cmd(self, cmd):
        self._print_account_state("Before withdrawal:")
        balance = self._get_balance(cmd)
        self._remove_from_source(cmd, balance)
        self._print_account_state("After withdrawal:")

    
    def execute_cmd(self, cmd):
        if (isinstance(cmd, CMDWithdraw)):
            self._execute_withdraw_cmd(cmd)
        elif (isinstance(cmd, CMDDonate)):
            self._execute_donate_cmd(cmd)
        else:
            raise AttributeError("Command not known/supported.")

    def teardown(self):
        self._conn.close()
