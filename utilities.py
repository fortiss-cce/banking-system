from typing import NamedTuple


class MoneyTransfer(NamedTuple):
    from_user: str
    to_user: str
    amount: float
