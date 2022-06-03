from domain import Database, Account, Money
class Banking():
    def __init__(self, database: Database):
        self.datasbase

    # banking helper functions
    def get_account_balance(self, account: Account) -> Money:
        return self.datasbase.get_account_balance(account)



    def donate(self, sender: Account, receiver: Account, amount: Money) -> str:


        balance_sender = self.get_account_balance(sender)
        balance_receiver = self.get_account_balance(receiver)

        # do checks if possible
        ######################

        self.update_account_balance(balance_sender, balance_sender.substract(amount))
        self.update_account_balance(balance_receiver, balance_receiver.add(amount))

        self.database.commit()
        
      

    def withdraw(self, account: Account , amount: Money) -> str: 

        balance_account = self.get_account_balance(account)
        # do checks if possible
        ######################

        self.update_account_balance(balance_account, balance_account.substract(amount))
        self.database.commit()

        
      