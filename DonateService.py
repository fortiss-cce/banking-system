from Service import Service
from Repository import Repository
from Controller import Controller


class DonateService(Service):

    def __init__(self, repository: Repository, controller: Controller):
        self.repository = repository
        self.controller = controller

    def donate(self):
        from_user = self.controller.get_from_user()
        to_user = self.controller.get_to_user()
        amount = self.controller.get_amount()

        print("Before donation:")
        self.repository.print_all()

        cursor = self.repository.get_balance(user=from_user)
        balance1 = 0
        for row in cursor:
            balance1 = row[0]
        self.repository.update_balance(amount=(balance1 - amount), user=from_user)
        cursor = self.repository.get_balance(user=to_user)
        balance2 = 0
        for row in cursor:
            balance2 = row[0]
        self.repository.update_balance(amount=(balance2 + amount), user=to_user)
        self.repository.update()

        print("\nAfter donation:")
        self.repository.print_all()

        self.repository.disconnect()