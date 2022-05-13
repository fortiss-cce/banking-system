

from dataclasses import dataclass

@dataclass
class Account:
    name: str
    balance: float

    def __str__(self):
        return f'NAME = {self.name};\tBALANCE = {self.balance}'
