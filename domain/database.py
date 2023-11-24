from abc import ABC, abstractmethod
from user import User
from bank_account import BankAccount

class Database(ABC):

	def add_money(user_id, amount, currency):
		pass

	def get_account_ids(user_id) -> list[int]:
		pass