# Import 

from src.User.user import User
from utils.bank_functions import *

# Class

class BankUser(User):
    """ A class for creating bank users. """

    def __init__(self, first_name, last_name, initial_balance, ID) -> None:
        """ Construct user. """
        self.first_name = first_name
        self.last_name = last_name
        self.balance : float = initial_balance
        self.ID = ID


    def get_balance(self) -> float:
        """ Returns user balance. """
        return self.balance

    def set_balance(self, amount : float) -> None:
        """ Set balance based on action. """
        self.balance += amount 

    def get_ID(self) -> str:
        """ Get bank user ID. """
        return self.ID