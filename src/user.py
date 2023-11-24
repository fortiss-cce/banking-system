class User():
    _uid     = ""
    _balance = 0

    def __init__(self, name, balance):
        self._uid = name
        self._balance = balance

    def remove(self, amount):
        if (amount > self._balance):
            self._balance -= amount
        else:
            raise AttributeError("Denied: going broke!")

    def add(self, amount):
        self._balance += amount

    def print_state(self):
        print("NAME = ", self._uid, ";\tBALANCE = ", self._balance)
