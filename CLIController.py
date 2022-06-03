from Controller import Controller
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
class CLIController(Controller):

    def __init__(self, __doc__):
        self.args = docopt(__doc__)
        self.print_arguments()
        self.type = 'CLI'

    def print_arguments(self):
        pprint.pprint(self.args)

    def get_from_user(self) -> str:
        return self.args["<from_user>"]

    def get_to_user(self) -> str:
        return self.args["<to_user>"]

    def get_amount(self) -> float:
        return float(self.args["<amount>"])

    def get_user(self) -> str:
        return self.args["<user>"]