
import pprint
from docopt import docopt

import storage_sqlite as storage
import operations

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
    db: storage.Storage = storage.initialise()

    storage.account_insert(db, Account('MagazinRoyale', 1000.00))
    storage.account_insert(db, Account('FynnKliemann', 1000.00))
    storage.account_insert(db, Account('Peter', 1000000.00))
    storage.account_insert(db, Account('Johannes', 1.00))
    
    args = docopt(__doc__)
    pprint.pprint(args)

    for op in operations.operations():
        if not args[op.name]: continue
        operations.execute(op, db, [args[i] for i in op.args])
        
    storage.close(db)
