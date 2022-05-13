
import sqlite3

import storage_base
from data import Account

class Storage(storage_base.Storage): pass

def initialise() -> Storage:
    db = Storage()
    db.conn = sqlite3.connect('./banking.db')
    return db

def account_insert(db: Storage, account: Account) -> None:
    stmt: str = 'insert or ignore into account (name, balance) values (?, ?);'
    db.conn.execute(stmt, (account.name, account.balance))
        
    
def account_get(db: Storage, name: str) -> Account:
    cursor = db.conn.execute('select balance from account where name = ?;', (name,))
    return next(cursor)[0]
    
def account_update(db: Storage, name: str, balance_new: float) -> None:
    db.conn.execute('update account set balance = ? where name = ?;', (balance_new, name,))
    
def account_list(db: Storage) -> list[Account]:
    cursor = db.conn.execute('select name, balance from account;')
    return [Account(i[0], i[1]) for i in cursor]
    
def commit(db: Storage) -> None:
    db.conn.commit()

def close(db: Storage) -> None:
    db.conn.close()
    db.conn = None
