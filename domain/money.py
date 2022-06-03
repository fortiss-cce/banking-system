
class Money():
    amount: float
    current_currency: str
    conversion_rates: dict
    def __init__(self, amount: float):
        self.amount = amount
    def substract(self, amount : "Money"):
        self.amount = self.amount - amount.amount
    def add(self, amount : "Money"):
        self.amount = self.amount + amount.amount
    def convert_amount(self, target_currency: str):
        raise NotImplementedError
   