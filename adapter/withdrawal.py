from application.bank_action import BankAction
from domain.bank_repository import BankRepository


class Withdrawal(BankAction):
    def __init__(self):
        pass

    def action(self, from_user:str, amount:float, repository:BankRepository):
        
        cursor = repository.get_database()

        print("Before withdrawal:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        cursor = repository.get_balance(from_user)
        balance_from_user = 0
        for row in cursor:
            balance_from_user = row[0]
        new_balance = balance_from_user - amount
        repository.update_account(from_user, new_balance)

        repository.commit()

        cursor = repository.get_database()

        print("\nAfter withdrawal:")
        for row in cursor:
            print("NAME = ", row[0], ";\tBALANCE = ", row[1])

        repository.close_connection()