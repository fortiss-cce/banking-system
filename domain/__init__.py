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

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Account(ABC):
    username: str
    balance: float

    @abstractmethod
    def set_balance(self, balance: float):
        pass

    @abstractmethod
    def get_balance(self, balance: float):
        pass


@dataclass
class Transaction(ABC):
    user: Account
    amount: float


@dataclass
class OutgoingTransaction:
    pass


@dataclass
class IncomingTransaction:
    pass


class DataStore(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def execute_transactions(self, transactions: list[Transaction]):
        pass

    def get_account_info(self) -> list[Account]:
        pass

    @abstractmethod
    def teardown(self):
        pass