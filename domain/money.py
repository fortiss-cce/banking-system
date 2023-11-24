from abc import ABC, abstractmethod

class Money(ABC):
	amount : float

	def __init__(self, amount) -> None:
		self.amount = amount
		
	@abstractmethod
	def get_amount(self):
		pass

	@abstractmethod
	def get_currency(self):
		pass

