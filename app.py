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

from use_cases import DonateService, WithdrawService, PrintAllService, \
    GetUser

if __name__ == '__main__':
    args = docopt(__doc__)
    pprint.pprint(args)

    if args["donate"]:
        # user1 = 'MagazinRoyale'  # this should be argument #1
        # user2 = 'FynnKliemann'  # this should be argument #2
        # amount = 100  # this should be argument #3
        from_user = GetUser().get_user(args["<from_user>"])
        to_user = GetUser().get_user(args["<to_user>"])
        amount = float(args["<amount>"])

        PrintAllService().printAllUsers("Before donation:")
        DonateService().donate(from_user, to_user, amount)
        PrintAllService().printAllUsers("After donation:")

    if args["withdraw"]:
        to_user = GetUser().get_user(args["<to_user>"])
        amount = float(args["<amount>"])

        PrintAllService().printAllUsers("Before withdrawal:")
        WithdrawService().transfer_amount(to_user, amount)
        PrintAllService().printAllUsers("After withdrawal:")
