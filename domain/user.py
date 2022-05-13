class User:
    def __init__(self, name: str) -> None:
        self._name = name

    def getName(self) -> str:
        return self._name
