
def print_balances(storage, conn, time: str):
    accounts = storage.getAllAccounts()
    print(f"{time} donation:")
    for row in accounts:
        print("NAME = ", row.name, ";\tBALANCE = ", row.balance)
