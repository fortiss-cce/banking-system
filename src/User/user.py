# Import 

from abc import abstractclassmethod

# Abstract class

class User():
    """ Abstract class for user. """


    @abstractclassmethod
    def get_user_information(self):
        """ Get basic information about user. """
        pass

    @abstractclassmethod
    def get_first_name(self):
        """ Get user first name. """
        pass

    @abstractclassmethod
    def get_last_name(self):
        """ Get user last name. """
        pass

    # Continue to add necessary functions for user ... 