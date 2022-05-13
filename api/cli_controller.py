from services.user_account_service import UserAccountService


def CLIController:

    def __init__(self, connection):
        self.service = UserAccountService(connection)

    def execute(self, args):

        if args["donate"]:
            from_user = args["<from_user>"]
            to_user = args["<to_user>"]
            amount = float(args["<amount>"])
            self.service.donate(from_user, to_user, amount)
        if args["withdraw"]:
            user = args["<user>"]
            amount = float(args["<amount>"])
            self.service.withdraw(user, amount)


