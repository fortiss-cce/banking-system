# Import



# Functions

def donate(donating_user, target_user, amount : float) -> None:
        """ User donate money from its own balance. """

        if exceed_balance(user = donating_user, amount = amount, action = 'Donate'):
            raise ValueError  
        else:
            donating_user.set_balance(-amount), target_user.set_balance(amount)



def withdraw(withdrawing_user, amount : float) -> None: 
    """ Withdraw money from bank account. """

    if exceed_balance(user = withdrawing_user, amount = amount, action = 'Withdraw'):
        raise ValueError
    else:
        current_balance = withdrawing_user.get_balance() 
        withdrawing_user.set_balance(current_balance - amount) 


def exceed_balance(user, amount : float, action : str) -> bool:
    """ Check if amount for donation of withdrawl exceeds current balance. """

    assert action in ['Withdraw', 'Donate']

    if amount > user.get_balance():
        print(f'{action} amount exceeds current balance. Please donate less. ')
        return True

    return False