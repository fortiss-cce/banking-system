import sqlite3
import pprint
from docopt import docopt

__doc__ = """
Donation System
Usage:
    app.py donate --from <from_user> --to <to_user> --amount <amount>
    app.py withdraw --user <user> --amount <amount>

Options:
    -f, --from             The user from which bank account is donated.
    -t, --to               The user to which bank account is donated.
    -u, --user             The user wanting to withdraw money from his/her account.
    -a, --amount           The amount handled by the command.
    
Existing accounts:
    * MagazinRoyale
    * FynnKliemann
    * Peter
    * Johannes
"""

if __name__ == '__main__':
    conn = sqlite3.connect('./banking.db')

    conn.execute("CREATE TABLE IF NOT EXISTS ACCOUNT (NAME TEXT PRIMARY KEY NOT NULL, BALANCE REAL NOT NULL);")
    conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('MagazinRoyale', 1000.00 );")
    conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('FynnKliemann', 1000.00 )")
    conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Peter', 1000000.00 )")
    conn.execute("INSERT OR IGNORE INTO ACCOUNT (NAME, BALANCE) VALUES ('Johannes', 1.00 )")
    conn.commit()

    args = docopt(__doc__)
    pprint.pprint(args)

    if args["donate"]:
        # user1 = 'MagazinRoyale'  # this should be argument #1
        # user2 = 'FynnKliemann'  # this should be argument #2
        # amount = 100  # this should be argument #3
        from_user = args["<from_user>"]
        to_user = args["<to_user>"]
        amount = float(args["<amount>"])

        cursor = conn.execute("SELECT * from ACCOUNT")
        print("Before donation:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (from_user,))
        balance1 = 0
        for row in cursor:
            balance1 = row[0]
        conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance1 - amount), from_user,))

        cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (to_user,))
        balance2 = 0
        for row in cursor:
            balance2 = row[0]
        conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance2 + amount), to_user,))

        conn.commit()

        cursor = conn.execute("SELECT * from ACCOUNT;")
        print("\nAfter donation:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        conn.close()

    if args["withdraw"]:
        user = args["<user>"]
        amount = float(args["<amount>"])

        cursor = conn.execute("SELECT * from ACCOUNT;")
        print("Before withdrawal:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        cursor = conn.execute("SELECT BALANCE FROM ACCOUNT WHERE NAME = ?;", (user,))
        balance = 0
        for row in cursor:
            balance = row[0]
        conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance - amount), user,))

        conn.commit()

        cursor = conn.execute("SELECT * from ACCOUNT;")
        print("\nAfter withdrawal:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        conn.close()
