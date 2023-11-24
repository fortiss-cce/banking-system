from domain.balance_change import BalanceChange


class History:

    trade: list[BalanceChange]
    def __init__(self, trade):
        self.trade = trade