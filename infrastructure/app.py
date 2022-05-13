import pprint
from docopt import docopt

from DB_Service import Broker, SqlBroker
from utilities import DEMO_DB_SETUP, MoneyTransfer, STORAGE_PATH
from storage import StorageSqlite

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


def print_user_balances(brk: Broker, *users):
    for usr in users:
        print("NAME = ", usr, ";\tBALANCE = ", brk.user_balance(usr))


if __name__ == '__main__':
    args = docopt(__doc__)
    pprint.pprint(args)

    with StorageSqlite(STORAGE_PATH) as storage:
        storage.execute_statements(DEMO_DB_SETUP)
        broker = SqlBroker(storage)

        if args["donate"]:
            transfer = MoneyTransfer(args["<from_user>"], args["<to_user>"], float(args["--amount"]))

            print("Before donation:")
            print_user_balances(broker, transfer.from_user, transfer.to_user)
            broker.transfer(transfer)
            print("After donation:")
            print_user_balances(broker, transfer.from_user, transfer.to_user)

        if args["withdraw"]:
            broker = SqlBroker(storage)
            user = args["<user>"]
            amount = float(args["<amount>"])

            print("Before withdrawal:")
            print_user_balances(user)
            broker.withdraw(user, amount)
            print("\nAfter withdrawal:")
            print_user_balances(user)
