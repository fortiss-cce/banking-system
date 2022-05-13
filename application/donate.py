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


from ..domain.core import Transaction, IncomingTransaction, OutgoingTransaction, Account
from ..domain.action import Action


class DonateAction(Action):
    def __init__(self, from_account: Account, to_account: Account, amount: float):
        super().__init__()
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def steps(self) -> list[Transaction]:
        return [
            OutgoingTransaction(self.from_account, self.amount),
            IncomingTransaction(self.to_account, self.amount),
        ]
