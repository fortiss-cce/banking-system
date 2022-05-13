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

from application.donateservice import DonateService

from application.withdrawservice import WithdrawService

from application.printallservice import PrintAllAccountsService
from infrastructure.SQLStorage import SQLStorage

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

    storage = SQLStorage(conn)
    print_service = PrintAllAccountsService(storage)

    if args["donate"]:
        # user1 = 'MagazinRoyale'  # this should be argument #1
        # user2 = 'FynnKliemann'  # this should be argument #2
        # amount = 100  # this should be argument #3
        from_user = args["<from_user>"]
        to_user = args["<to_user>"]
        amount = float(args["<amount>"])

        print_service.print_balances("Before")
        donate_service = DonateService(storage)

        donate_service.donate(from_user, to_user, amount)

        conn.commit()
        conn.close()

        print_service.print_balances("After")

    if args["withdraw"]:
        user = args["<user>"]
        amount = float(args["<amount>"])

        print_service.print_balances("Before")

        withdraw_service = WithdrawService(storage)

        withdraw_service.withdraw(user, amount)

        conn.commit()
        conn.close()

        print_service.print_balances("After")