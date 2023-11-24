from money import Money

class BankAccount:
	money : Money
	id

	def set_money(self, new_money : Money):
		self.money = new_money

	def get_money(self):
		return self.money
