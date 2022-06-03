# Import 

from abc import abstractclassmethod

# Abstract class

class Interface: 
    """ Abstract class for general purpose interface. """

    @abstractclassmethod
    def get_user_arguments(self) -> None: 
        """ Get user arguments from interface. """
        pass

    @abstractclassmethod
    def create_output(self):
        """ Creates output for specific actions. """
        pass

    