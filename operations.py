
from dataclasses import dataclass

import storage
from data import Account


@dataclass
class Operation:
    name: str
    args: list[str]
    _executor: Callable[[storage.Storage, list[str]], None]

def _print_all_accounts(db: storage.Storage) -> None:
    for account in storage.account_list(db):
        print(account)    
    
def execute_donate(db: storage.Storage, args: list[str]) -> None:
    # user1 = 'MagazinRoyale'  # this should be argument #1
    # user2 = 'FynnKliemann'  # this should be argument #2
    # amount = 100  # this should be argument #3
    from_user, to_user, amount = args
    amount = float(amount)

    print("Before donation:")
    _print_all_accounts(db)

    balance1 = storage.account_get(db, from_user)
    balance2 = storage.account_get(db, to_user)

    storage.account_update(db, from_user, balance1 - amount)
    storage.account_update(db, to_user,   balance2 - amount)

    storage.commit(db)

    print("\nAfter donation:")
    _print_all_accounts(db)


def execute_withdraw(db: storage.Storage, args: list[str]) -> None:
    user, amount = args
    amount = float(amount)
   
    print("Before withdrawal:")
    _print_all_accounts(db)

    balance = storage.account_get(db, user)

    storage.account_update(db, user, balance - amount)

    print("\nAfter withdrawal:")
    _print_all_accounts()
    
operations: list[Operation] = [
    Operation('donate', ["<from_user>", "<to_user>", "<amount>"], execute_donate),
    Operation('withdraw', ["<user>", "<amount>"], execute_withdraw),
]

def execute(operation: Operation, db: storage.Storage, args: list[str]) -> None:
    operation._executor(db, args)
