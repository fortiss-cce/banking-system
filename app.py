import pprint
from docopt import docopt

from DB_Service import SqlBroker
from utilities import MoneyTransfer

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


def print_user_balances(*users):
    for user in users:
        print("NAME = ", user, ";\tBALANCE = ", broker.user_balance(user))


if __name__ == '__main__':
    broker = SqlBroker()

    args = docopt(__doc__)
    pprint.pprint(args)

    if args["donate"]:
        transfer = MoneyTransfer(args["--from"], args["--to"], float(args["--amount"]))

        print("Before donation:")
        print_user_balances(transfer.from_user, transfer.to_user)
        broker.transfer(transfer)
        print("After donation:")
        print_user_balances(transfer.from_user, transfer.to_user)

    if args["withdraw"]:
        user = args["<user>"]
        amount = float(args["<amount>"])

        print("Before withdrawal:")
        print_user_balances(user)
        broker.withdraw(user, amount)
        print("\nAfter withdrawal:")
        print_user_balances(user)

        conn.close()
