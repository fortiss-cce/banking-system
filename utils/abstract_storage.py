import abc


class AbstractStorage(abc.ABC):
    def get_connection(self):
        raise NotImplementedError

    def insert_mock_data(self, conn):
        raise NotImplementedError

    def close_connection(self, conn):
        raise NotImplementedError
