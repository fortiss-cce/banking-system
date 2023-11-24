from abc import ABC


class CMD(ABC):
    _from_user = ""
    _to_user   = ""
    _amount    = 0

class CMDDonate(CMD):

    def __init__(self, dictionary):
        self._from_user = dictionary["<from_user>"]
        self._to_user   = dictionary["<to_user>"]
        self._amount    = float(dictionary["<amount>"])

class CMDWithdraw(CMD):
   
    def __init__(self, dictionary):
        self._from_user = dictionary["<user>"]
        self._amount    = dictionary["<amount>"]

class CMDFactory():

    @staticmethod
    def generate_cmd(dictionary):
        if (dictionary["donate"]):
            return CMDDonate(dictionary)
        elif (dictionary["withdraw"]):
            return CMDWithdraw(dictionary)
        else:
            raise AttributeError("Command not known/supported.")
