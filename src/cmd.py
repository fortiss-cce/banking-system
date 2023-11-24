from abc import ABC, abstractmethod
from user import User
from database import DataBase

class CMD(ABC):
    _from_user = User(None, None)
    _amount    = 0

    @abstractmethod
    def execute():
        pass

class CMDDonate(CMD):
    _to_user = User(None, None)

    def __init__(self, dictionary):
        self._from_user = DataBase.get_user(dictionary["<from_user>"])
        self._to_user   = DataBase.get_user(dictionary["<to_user>"])
        self._amount    = float(dictionary["<amount>"])

    def execute(self):
        self._from_user.remove(self._amount)
        DataBase.update_user(self._from_user)
        self._to_user.add(self._amount)
        DataBase.update_user(self._to_user)

class CMDWithdraw(CMD):
   
    def __init__(self, dictionary):
        self._from_user = DataBase.get_user(dictionary["<user>"])
        self._amount    = dictionary["<amount>"]

    def execute(self):
        self._from_user.remove(self._amount)
        DataBase.update_user(self._from_user)

class CMDFactory():

    @staticmethod
    def generate_cmd(dictionary):
        if (dictionary["donate"]):
            return CMDDonate(dictionary)
        elif (dictionary["withdraw"]):
            return CMDWithdraw(dictionary)
        else:
            raise AttributeError("Command not known/supported.")
