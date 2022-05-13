import abc
from domain.user_account import UserAccount


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_account_balance(self, user_account: UserAccount):
        raise NotImplementedError

    @abc.abstractmethod
    def update_account_balance_by_name(self, user_account: UserAccount, new_balance: float):
        raise NotImplementedError
