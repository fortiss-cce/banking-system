from Controller import Controller
from Repository import Repository
from Service import Service
from SQLRepository import SQLRepository
from CLIController import CLIController
from DonateService import DonateService
from WithdrawService import WithdrawService
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
    filename = './banking.db'
    repository = SQLRepository(filename=filename)
    controller = CLIController(__doc__)
    if controller.args["donate"]:
        DonateService(repository=repository, controller=controller).donate()
    elif controller.args["withdraw"]:
        WithdrawService(repository=repository, controller=controller).withdraw()
    else:
        raise "I do not know what to do"



