from infrastructure.postgresql import BankSystemPostGreSQL
from infrastructure.sqlite import BankSystemSQLite
from application.donate import Donation
from application.loan import Loan
from application.withdraw import WithDraw

from domain.user import User
from typing import Union

class WebAPI:
    def __init__(self, bank_system:Union[BankSystemPostGreSQL, BankSystemSQLite]) -> None:
        pass
    
    def user_login(name:str, balance:float) -> User:
        pass

    def donate():
        pass

    def loan():
        pass

    def withdraw():
        pass
    

