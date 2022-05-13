import pprint
from docopt import docopt
import utils.sqlite_storage
from api.cli_controller import CLIController

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

    args = docopt(__doc__)
    pprint.pprint(args)

    connection = utils.sqlite_storage.SQLiteStorage()
    controller = CLIController(connection)
    controller.execute(args)
