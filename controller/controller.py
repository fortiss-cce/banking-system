from domain import Account, Money, Banking, Database, SQL, PostGresSQl

class Controller:
    _database_selection: str = "SQL"
    def __init__(self):
        pass

    def run_banking_service(self, sender: Account, receiver: Account, amount: Money, action: str) -> str:
        # do some checks
        if action == "donate":
            response = self.donate( sender, receiver, amount)

        elif action == "withdrawing":
            response = self.withdrawing( sender, amount)     
        else:
            raise ActionNotValid
        
        return response

    def donate(self, sender: Account, receiver: Account, amount: Money):
        database= self.setup_database(self._database_selection)
        banking = Banking(database = database)
        banking.donate( sender, receiver, amount)
        response =  self.close()
        return response


    def withdrawing(self,sender : Account , amount: Money):
        database= self.setup_database(self._database_selection)
        banking = Banking(database = database)
        banking.withdrawing( sender, amount)
        response =  self.close()
        return response

    def setup_database(self, database_selection: str) -> Database: 
        if self.database_selection == "SQL":
            database = SQL()
        else: 
            database = PostGresSQL()
        database.connect() 
        return database

    def close(self, database: Database): 
        database.commit()
        return database.close()

        
        