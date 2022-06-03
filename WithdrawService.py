from Service import Service
from  Repository import Repository
from Controller import Controller


class WithdrawService(Service):

    def __init__(self, repository: Repository, controller: Controller):
        self.repository = repository
        self.controller = controller

    def withdraw(self):
        user = self.controller.get_user()
        amount = self.controller.get_amount()
        print("Before withdrawal:")
        self.repository.print_all()

        cursor = self.repository.get_balance(user=user)
        balance = 0
        for row in cursor:
            balance = row[0]
        self.repository.update_balance(amount=(balance - amount), user=user)
        self.repository.update()

        print("\nAfter withdrawal:")
        self.repository.print_all()
        self.repository.disconnect()

