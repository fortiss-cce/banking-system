import pprint
from docopt import docopt
from adapter.donation import Donation

from adapter.sqlite_repository import SqlightRepository
from adapter.withdrawal import Withdrawal

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

    repository = SqlightRepository()

    args = docopt(__doc__)
    pprint.pprint(args)

    if args["donate"]:
        # user1 = 'MagazinRoyale'  # this should be argument #1
        # user2 = 'FynnKliemann'  # this should be argument #2
        # amount = 100  # this should be argument #3
        from_user = args["<from_user>"]
        to_user = args["<to_user>"]
        amount = float(args["<amount>"])

        donate_action = Donation()
        donate_action.action(from_user, to_user, amount, repository)

    if args["withdraw"]:
        user = args["<user>"]
        amount = float(args["<amount>"])

        donate_action = Withdrawal().action(user, amount, repository)
