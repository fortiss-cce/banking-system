import sqlite3
from . import Account, Money
class Database(): 

    @bastractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_all_accounts(self):
        pass

    @bastractmethod
    def get_account_balance(self, account: Account) -> Money:
        pass

    @bastractmethod
    def update_account_balance(self, account: Account, amount: Money):
        pass

    @abstractmethod
    def commit(self):
        pass


class SQL(Database):
    def connect(self):
        pass

   
    def get_all_accounts(self):
        pass

   
    def get_account_balance(self, account: Account) -> Money:
        pass

    
    def update_account_balance(self, account: Account, amount: Money):
        pass

   
    def commit(self):
        pass


class PostGresSQL(Database):
    def connect(self):
        pass

   
    def get_all_accounts(self):
        pass

   
    def get_account_balance(self, account: Account) -> Money:
        pass

    
    def update_account_balance(self, account: Account, amount: Money):
        pass

   
    def commit(self):
        pass