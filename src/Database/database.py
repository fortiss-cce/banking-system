# Import 

from abc import abstractclassmethod

# Abstract Class

class Database():
    """ Abstract class for database. """

    @abstractclassmethod
    def add_user(self) -> None:
        """ Add user to database. """
        pass

    @abstractclassmethod
    def delete_user(self) -> None:
        """ Delete user from database. """
        pass

    