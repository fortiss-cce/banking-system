class User:
    _name: str
    def __init__(self, name: str):
        self._name = name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name

