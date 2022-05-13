
from data import Account

class Storage: pass

def initialise() -> Storage: pass
def account_insert(db: Storage, account: Account) -> None: pass
def account_get   (db: Storage, name: str) -> Account: pass
def account_update(db: Storage, name: str, balance_new: float) -> None: pass
def account_list  (db: Storage) -> list[Account]: pass
def commit        (db: Storage) -> None: pass
def close         (db: Storage) -> None: pass
