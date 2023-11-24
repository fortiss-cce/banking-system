from abc import ABCMeta, abstractmethod


class IStorage:
    __metaclass__ = ABCMeta

    def __init__(self, instance):
        self.instance = instance

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def select(self):
        pass


class Sqlite(IStorage):

    def create(self):
        raise NotImplementedError('In progress')

    def insert(self):
        raise NotImplementedError('In progress')

    def update(self):
        raise NotImplementedError('In progress')

    def select(self):
        raise NotImplementedError('In progress')

class Postgresql(IStorage):
    raise NotImplementedError('In progress')