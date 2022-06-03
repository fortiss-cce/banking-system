
import argparse
import pprint
from docopt import docopt

from domain import Account, Money
from controller import Controller


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


def parser():
    arguments = argparse.parse_args()
    sender = Account(arguments["from"])
    receiver = Account(arguments.to)
    amount = Money(arguments.amount)
    action = arguments.action
    return sender, receiver, amount, action


if __name__=='__main__':

    #obtaining input arguments
    sender, receiver, amount, action = parser()
    result = Controller().run_banking_service(sender, receiver, amount, action)

    # do sth with result
    api_response = "..."
    print(api_response)



