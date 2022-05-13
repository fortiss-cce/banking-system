
from data import Account

class Storage: pass

def initialise() -> Storage: pass
def account_insert(storage: Storage, account: Account): pass
def account_get   (storage: Storage, name: str) -> Account: pass
def account_update(storage: Storage, name: str, balance_new: float) -> Account: pass
def account_list  (storage: Storage) -> list[Account]: pass

