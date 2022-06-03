from abc import ABC


class Repository(ABC):
    pass

    def get_full_data(self):
        pass

    def get_balance(self, user: str):
        pass

    def update_balance(self, amount: float, user: str):
        pass

    def update(self):
        pass

    def print_all(self):
        pass

    def disconnect(self):
        pass
