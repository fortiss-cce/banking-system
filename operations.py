
from dataclasses import dataclass

import storage
from data import Account


@dataclass
class Operation:
    name: str
    args: list[str]
    _executor: Callable[[storage.Storage, list[str]], None]

def execute_donate(db: storage.Storage, args: list[str]) -> None:
    # user1 = 'MagazinRoyale'  # this should be argument #1
    # user2 = 'FynnKliemann'  # this should be argument #2
    # amount = 100  # this should be argument #3
    from_user, to_user, amount = args
    amount = float(amount)

    print("Before donation:")
    for account in storage.account_list(db):
        print(account)

    balance1 = storage.account_get(db, from_user)
    balance2 = storage.account_get(db, to_user)

    storage.account_update(
    
    conn.execute("UPDATE ACCOUNT SET BALANCE = ? WHERE NAME = ?;", ((balance2 + amount), to_user,))

    conn.commit()

    cursor = conn.execute("SELECT * from ACCOUNT;")
    print("\nAfter donation:")
    for row in cursor:
        print("NAME = ", row[0], ";\tBALANCE = ", row[1])

    conn.close()


def execute_withdraw(db: storage.Storage, args: list[str]) -> None: pass

    
operations: list[Operations] = [
    Operation('donate', ["<from_user>", "<to_user>", "<amount>"], execute_donate),
    Operation('withdraw', ["<user>", "<amount>"], execute_withdraw),
]

def execute(operation: Operation, db: storage.Storage, args: list[str]) -> None:
    operation._executor(db, args)
