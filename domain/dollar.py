from money import Money

class Dollar(Money):

	def __init__(self, amount) -> None:
		super().__init__(amount)
		
	def get_amount(self):
		return self.amount

	def get_currency(self):
		return "USD"