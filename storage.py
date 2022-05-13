import sqlite3

class storage():
    


    def storage_connect(storage_path: str):  
        pass

    def storage_excecute(storage_execute_str: str):
        pass

    def storage_commit():
        pass

    def storage_close():
        pass

    def __enter__(self):
        self.storage_connect()

    def __exit__(selfe, type, value, tb):
        self.storage_close()


class storage_sqlite3(storage):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def storage_connect(self):
        conn = sqlite3.connect(self.storage_path)

    def storage_excecute(storage_execute_str: str):
        conn.execute(storage_execute_str)

    def storage_commit():
        conn.commit()

    def storage_close():
        conn.close()



       