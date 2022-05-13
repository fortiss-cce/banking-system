import abc
from typing import Iterable

import sqlite3


class Storage(abc.ABC):

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def terminate(self):
        pass

    @abc.abstractmethod
    def execute(self, statement: str):
        pass

    @abc.abstractmethod
    def execute_statements(self, statements: Iterable[str]):
        pass

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, type, value, tb):
        self.terminate()


class StorageSqlite(Storage):

    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.conn = None

    def _commit(self):
        self.conn.commit()

    def connect(self):
        self.conn = sqlite3.connect(self.storage_path)

    def execute(self, statement: str):
        if self.conn is None:
            raise ValueError("Storage not initialized")
        self.conn.execute(statement)
        self._commit()

    def execute_statements(self, statements: Iterable[str]):
        if self.conn is None:
            raise ValueError("Storage not initialized")
        for statement in statements:
            self.conn.execute(statement)
        self._commit()

    def terminate(self):
        if self.conn is None:
            raise ValueError("Storage not initialized")
        self.conn.close()
        self.conn = None
