from docopt import docopt

from bank_domain import Account
from bank_application import BankService
from bank_adapter import SQLiteStore

__doc__ = """
Donation System
Usage:
    app.py list
    app.py transfer --from <from_user> --to <to_user> --amount <amount>
    app.py withdraw --user <user> --amount <amount>

Options:
    -f, --from             The user from which bank account is transferred.
    -t, --to               The user to which bank account is transferred.
    -u, --user             The user wanting to withdraw money from his/her account.
    -a, --amount           The amount handled by the command.
    
Existing accounts:
    * MagazinRoyale
    * FynnKliemann
    * Peter
    * Johannes
"""

def setup_dummy_bank_service(bank: BankService):
    bank.create_account(Account('MagazinRoyale', 1000.00))
    bank.create_account(Account('FynnKliemann', 1000.00))
    bank.create_account(Account('Peter', 1000000.00))
    bank.create_account(Account('Johannes', 1.00))

if __name__ == '__main__':
    store = SQLiteStore('./banking.db')
    bank = BankService(store)
    bank.prepare()
    setup_dummy_bank_service(bank)

    args = docopt(__doc__)
    try:
        if args["transfer"]:
            from_user = args["<from_user>"]
            to_user = args["<to_user>"]
            amount = float(args["<amount>"])
            from_account, to_account = bank.transfer_money(from_user, to_user, amount)
            print("Transferred money:")
            print(f"{from_account.name.ljust(30)} {from_account.balance + amount} - {amount}")
            print(f"{to_account.name.ljust(30)} {to_account.balance - amount} + {amount}")

        elif args["withdraw"]:
            from_user = args["<from_user>"]
            amount = float(args["<amount>"])
            from_account = bank.withdraw_money(from_user, amount)
            print("Withdrew money:")
            print(f"{from_account.name.ljust(30)} {from_account.balance + amount} - {amount}")

        elif args["list"]:
            accounts = bank.retreive_accounts()
            for account in accounts:
                print(f"{account.name.ljust(30)} {account.balance}")

    except ValueError as e:
        print(e)