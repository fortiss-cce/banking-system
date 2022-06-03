# Import 

# Class

class UserDatabase: 
    """ A database containing all users of the bank. """

    def __init__(self, database_type, database_path) -> None: # Check how to add database type as input
        self.database_type = database_type
        self.database_path = database_path

    def add_user(self, user) -> None: 
        """ Add user to database. """
        pass

    def delete_user(self, user) -> None: 
        """ Delete user from database. """
        pass 

    def update_database(self, action, user, target_user = None) -> None: 
        """ Update database based on action [add, delete, donate, withdraw] """

        assert action in ['add', 'delete', 'withdraw', 'donate']

        if action == 'add':
            self.add_user(user = user)
        elif action == 'delete':
            self.delete_user(user = user)
        elif action == 'withdraw':
            self._update_balance(user = user)
        else:
            assert target_user is not None
            self._update_balance(user = user), self._update_balance(user = target_user)
        

    def _update_balance(self, user) -> None:
        """ Update balance for user in database. """
        # Search for user in database, update balance for specific user 
        
    # Database should be able to change format from SQLite to PostGreSQL