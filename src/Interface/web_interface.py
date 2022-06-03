# Import 

from Interface.interface import Interface

# Class -> DocOpt can be used as current Web Interface

class WebInterface(Interface):
    """ Class for web interface. """

    def __init__(self, web_option) -> None:
        super().__init__()
        self.web_option = web_option


    def get_user_arguments(self) -> None:
        """ Get necessary user arguments. """
        # Ideas are in a dictionary, list 

    
    def create_output(self, action) -> None: 
        """ Creates output for a specific bank action. """