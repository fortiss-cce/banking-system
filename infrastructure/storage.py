from abc import abstractmethod


class IStorage:

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
    pass

class Postgresql(IStorage):
    NotImplementedError('In progress')