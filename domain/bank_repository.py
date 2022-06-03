from abc import ABC, abstractmethod

from domain.user import User
 
class BankRepository(ABC):
 
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def insert_user(self, user: User):
        pass

    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def get_user_by_name(self, user_name: str):
        pass

    @abstractmethod
    def get_database(self):
        pass

    @abstractmethod
    def get_balance(self, user_name:str):
        pass

    @abstractmethod
    def update_account(self, user_name:str, balance:float):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass