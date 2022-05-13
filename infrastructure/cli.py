import pprint
from docopt import docopt

from domain.bank import Bank
from domain.user import User
from infrastructure.sql_database import SQLDatabase

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


if __name__ == "__main__":
    args = docopt(__doc__)
    pprint.pprint(args)

    database = SQLDatabase("./banking.db")
    database.connect()
    database.addUser(User("MagazinRoyale", 1000.0))
    database.addUser(User("FynnKliemann", 1000.0))
    database.addUser(User("Peter", 1000000.0))
    database.addUser(User("Johannes", 1.0))
    database.closeDatabase()
    bank = Bank(database)

    if args["donate"]:
        # user1 = 'MagazinRoyale'  # this should be argument #1
        # user2 = 'FynnKliemann'  # this should be argument #2
        # amount = 100  # this should be argument #3
        from_user = User(args["<from_user>"])
        to_user = User(args["<to_user>"])
        amount = float(args["<amount>"])

        bank.donate(from_user, to_user, amount)

    if args["withdraw"]:
        user = User(args["<user>"])
        amount = float(args["<amount>"])
        bank.withdraw(user, amount)
