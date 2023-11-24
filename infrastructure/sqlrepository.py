from domain.repository import Repository

class SqLRepository(Repository):
    
    def addBankAccount(self, BankAccount):
        pass
    
    def getBankAccount(self, user: User):
        pass

    def updateBankAccount(self, user: User, new_balance: float):
        pass

    def getBalance(self, user: User):
        pass