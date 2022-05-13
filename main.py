# Copyright (C) 2022 RostLab
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pprint
from docopt import docopt

from .infrastructure.sqlite import SQLiteStore
from .domain.core import Account, Transaction
from .domain.data import DataStore
from .application.donate import DonateAction

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


def do_dontation(args: dict, data_store: DataStore, user_data):
    from_user_name = args["<from_user>"]
    to_user_name = args["<to_user>"]
    amount = float(args["<amount>"])
    from_account = data_store.get_account_for_username(from_user_name)
    to_account = data_store.get_account_for_username(to_user_name)
    action = DonateAction(from_account, to_account, amount)
    action.execute()


def do_withdraw(args: dict, data_store: DataStore):
    pass


COMMAND_DICT = {"donate": do_dontation, "withdraw": do_withdraw}


if __name__ == "__main__":

    args = docopt(__doc__)
    pprint.pprint(args)

    data_store = SQLiteStore()

    command = args["donate"]
