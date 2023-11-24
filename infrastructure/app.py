from abc import ABCMeta, abstractmethod

from domain.user import User


class app:
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def donate(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class web_api(app):

    user: User
    def __init__(self, user):
        self.user = user

    '''
    TODO: Implement/Include all callable functions, such as withdraw and donate
    '''
