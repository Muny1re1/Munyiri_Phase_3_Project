from .connection import (CONN, CURSOR)
from .setup import create_table

class Trader:
    def __init__(self, trader_name, id=None):
        create_table()
        self._trader_name = None
        self.trader_name = trader_name
        if id is None:
            self.id = self.save_to_db()
        else:
            self.id = id
    
    @property
    def trader_name(self):
        return self._trader_name
    
    @trader_name.setter
    def trader_name(self, trader_name):
        if self._trader_name is not None:
            raise AttributeError("Trader name has already been set!")
        if not (isinstance(trader_name, str) and len(trader_name) > 0):
            raise ValueError("Trader name must be a non-empty string!")
        self._trader_name = trader_name

    def save_to_db(self):
        sql = """
            INSERT INTO traders 
            (trader_name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.trader_name,))
        CONN.commit()
        return CURSOR.lastrowid

    def delete_from_db(self):
        sql = """
            DELETE FROM traders WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM traders
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM traders WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(row[1], row[0])
        return None