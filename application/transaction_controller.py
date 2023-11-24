from ../domain.database import Database
from exchange_controller import ExchangeController

class TransactionController:
	database : Database
	exchanger : ExchangeController
	
	def __init__(self, database : Database) -> None:
		self.database = database
		self.exchanger = ExchangeController()

	def donate_money(self, user_id, amount, currency):
		pass

	def withdraw_money(self, user_id, amount, currency):
		pass

	def load_money(self, user_id, amount, currency):
		pass

	def payoff_money(self, user_id, amount, currency):
		pass

	def exchange_money(self, user_id, amount, old_currency, new_currency):
		new_amount = self.exchanger.change_currency(amount, old_currency, new_currency)
		self.database.set_money(user_id, new_amount)
