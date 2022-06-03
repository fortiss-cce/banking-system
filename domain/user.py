

class User:
    _name: str
    _iban: str
    _bic: str
    _balance: float

    def __init__(self, name:str, iban:str, bic:str, savings: float):
        self._name = name
        self._iban = iban
        self._bic = bic
        self._balance = savings

    def get_name_of_user(self):
        return self._name

    def get_iban_of_user(self):
        return self._iban

    def get_bic_of_user(self):
        return self._bic

    def get_balance_of_user(self):
        return self._balance
